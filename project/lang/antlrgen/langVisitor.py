# Generated from lang.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

# This class defines a complete generic visitor for a parse tree produced by langParser.


class langVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by langParser#prog.
    def visitProg(self, ctx: langParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#stmt.
    def visitStmt(self, ctx: langParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#bind.
    def visitBind(self, ctx: langParser.BindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#lambda.
    def visitLambda(self, ctx: langParser.LambdaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#print.
    def visitPrint(self, ctx: langParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#var.
    def visitVar(self, ctx: langParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#Int.
    def visitInt(self, ctx: langParser.IntContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#String.
    def visitString(self, ctx: langParser.StringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#Set.
    def visitSet(self, ctx: langParser.SetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#Range.
    def visitRange(self, ctx: langParser.RangeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#kleeneStar.
    def visitKleeneStar(self, ctx: langParser.KleeneStarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#addFinal.
    def visitAddFinal(self, ctx: langParser.AddFinalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#intersect.
    def visitIntersect(self, ctx: langParser.IntersectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#in.
    def visitIn(self, ctx: langParser.InContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#vertices.
    def visitVertices(self, ctx: langParser.VerticesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#unify.
    def visitUnify(self, ctx: langParser.UnifyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#edges.
    def visitEdges(self, ctx: langParser.EdgesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#setStarts.
    def visitSetStarts(self, ctx: langParser.SetStartsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#smb.
    def visitSmb(self, ctx: langParser.SmbContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#setFinals.
    def visitSetFinals(self, ctx: langParser.SetFinalsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#concat.
    def visitConcat(self, ctx: langParser.ConcatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#valExpr.
    def visitValExpr(self, ctx: langParser.ValExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#reachable.
    def visitReachable(self, ctx: langParser.ReachableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#brackets.
    def visitBrackets(self, ctx: langParser.BracketsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#labels.
    def visitLabels(self, ctx: langParser.LabelsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#filter.
    def visitFilter(self, ctx: langParser.FilterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#varExpr.
    def visitVarExpr(self, ctx: langParser.VarExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#load.
    def visitLoad(self, ctx: langParser.LoadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#finals.
    def visitFinals(self, ctx: langParser.FinalsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#addStarts.
    def visitAddStarts(self, ctx: langParser.AddStartsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#starts.
    def visitStarts(self, ctx: langParser.StartsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by langParser#map.
    def visitMap(self, ctx: langParser.MapContext):
        return self.visitChildren(ctx)


del langParser
