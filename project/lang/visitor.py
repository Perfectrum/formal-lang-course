from antlr4 import *
from typing import TextIO

if "." in __name__:
    from .antlrgen.langParser import langParser
    from .antlrgen.langLexer import langLexer
    from .antlrgen.langVisitor import langVisitor
    from ..graph_utils import get_graph
    from ..graph_regular_query import get_reachable_vertices
    from .lang_types import Graph
else:
    from antlrgen.langParser import langParser
    from antlrgen.langLexer import langLexer
    from antlrgen.langVisitor import langVisitor
    from ..graph_utils import get_graph
    from ..graph_regular_query import get_reachable_vertices
    from .lang_type import Graph


class Visitor(langVisitor):
    def __init__(self, writer: TextIO = None):
        self.writer = writer
        self.context = {}

    def visitPrint(self, ctx: langParser.PrintContext):
        variable = self.visit(ctx.getChild(1))

        output = str(variable).replace("'", '"')

        if isinstance(variable, set) and len(variable) == 0:
            output = "{}"

        print(output, file=self.writer)

        return self.defaultResult()

    def visitString(self, ctx: langParser.StringContext):
        return ctx.getText()[1:-1]

    def visitInt(self, ctx: langParser.IntContext):
        return int(ctx.getText())

    def visitBind(self, ctx: langParser.BindContext):
        name = ctx.getChild(0).getText()
        value = self.visitExpr(ctx.expr())
        self.context[name] = value
        return self.defaultResult()

    def visitExpr(self, ctx: langParser.ExprContext):
        if ctx.getChild(0).getText() == "load":
            return self.visitLoad(ctx)

        if ctx.getChild(0).getText() == "set":
            return self.visitSetStarts(ctx)

        return self.visitChildren(ctx)

    def visitVar(self, ctx: langParser.VarContext):
        return self.context[ctx.getText()]

    def visitSet(self, ctx: langParser.SetContext):
        return {self.visit(ctx.getChild(x)) for x in range(1, ctx.getChildCount(), 2)}

    def visitRange(self, ctx: langParser.RangeContext):
        left = int(ctx.getChild(1).getText())
        right = int(ctx.getChild(3).getText())
        return set(range(left, right))

    def visitLoad(self, ctx: langParser.LoadContext):
        return Graph(get_graph(ctx.getChild(1).getText()[1:-1]))

    def visitStarts(self, ctx: langParser.StartsContext):
        return self.context[ctx.getChild(0).getText()].starts

    def visitFinals(self, ctx: langParser.FinalsContext):
        return self.context[ctx.getChild(0).getText()].finals

    def visitEdges(self, ctx: langParser.EdgesContext):
        return self.context[ctx.getChild(0).getText()].get_edges()

    def visitVertices(self, ctx: langParser.EdgesContext):
        return self.context[ctx.getChild(0).getText()].get_vertices()

    def visitLabels(self, ctx: langParser.LabelsContext):
        return self.context[ctx.getChild(0).getText()].get_labels()

    def visitSetStarts(self, ctx: langParser.SetStartsContext):
        starts = self.visit(ctx.getChild(1))
        graph = self.visit(ctx.getChild(5))
        graph.set_starts(starts)
        return graph

    def visitSetFinals(self, ctx: langParser.SetStartsContext):
        finals = self.visit(ctx.getChild(1))
        graph = self.visit(ctx.getChild(5))
        graph.set_finals(finals)
        return graph

    def visitIn(self, ctx: langParser.InContext):
        what = self.visit(ctx.getChild(0))
        if not isinstance(what, set):
            what = {what}

        where = self.visit(ctx.getChild(2))
        if not isinstance(where, set):
            what = {where}

        return int(what.issubset(where))

    def visitLambda(self, ctx: langParser.LambdaContext):
        var = ctx.getChild(1).getText()
        body = ctx.getChild(3)

        def func(x):
            prev_var = None
            if var in self.context:
                prev_var = self.context[var]
            self.context[var] = x
            res = self.visit(body)
            if prev_var is not None:
                self.context[var] = prev_var
            else:
                self.context.pop(var)
            return res

        return func

    def visitMap(self, ctx: langParser.MapContext):
        s = self.visit(ctx.getChild(1))
        f = self.visit(ctx.getChild(3))
        return list(map(int, map(f, s)))

    def visitFilter(self, ctx: langParser.FilterContext):
        s = self.visit(ctx.getChild(1))
        f = self.visit(ctx.getChild(3))
        return list(filter(f, s))

    def visitReachable(self, ctx: langParser.ReachableContext):
        graph = self.visit(ctx.getChild(2))
        return graph.reachable()

    def visitBrackets(self, ctx: langParser.BracketsContext):
        return self.visit(ctss.getChild(1))
