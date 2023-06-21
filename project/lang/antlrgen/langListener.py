# Generated from lang.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser


# This class defines a complete listener for a parse tree produced by langParser.
class langListener(ParseTreeListener):
    # Enter a parse tree produced by langParser#prog.
    def enterProg(self, ctx: langParser.ProgContext):
        pass

    # Exit a parse tree produced by langParser#prog.
    def exitProg(self, ctx: langParser.ProgContext):
        pass

    # Enter a parse tree produced by langParser#stmt.
    def enterStmt(self, ctx: langParser.StmtContext):
        pass

    # Exit a parse tree produced by langParser#stmt.
    def exitStmt(self, ctx: langParser.StmtContext):
        pass

    # Enter a parse tree produced by langParser#bind.
    def enterBind(self, ctx: langParser.BindContext):
        pass

    # Exit a parse tree produced by langParser#bind.
    def exitBind(self, ctx: langParser.BindContext):
        pass

    # Enter a parse tree produced by langParser#lambda.
    def enterLambda(self, ctx: langParser.LambdaContext):
        pass

    # Exit a parse tree produced by langParser#lambda.
    def exitLambda(self, ctx: langParser.LambdaContext):
        pass

    # Enter a parse tree produced by langParser#print.
    def enterPrint(self, ctx: langParser.PrintContext):
        pass

    # Exit a parse tree produced by langParser#print.
    def exitPrint(self, ctx: langParser.PrintContext):
        pass

    # Enter a parse tree produced by langParser#var.
    def enterVar(self, ctx: langParser.VarContext):
        pass

    # Exit a parse tree produced by langParser#var.
    def exitVar(self, ctx: langParser.VarContext):
        pass

    # Enter a parse tree produced by langParser#Int.
    def enterInt(self, ctx: langParser.IntContext):
        pass

    # Exit a parse tree produced by langParser#Int.
    def exitInt(self, ctx: langParser.IntContext):
        pass

    # Enter a parse tree produced by langParser#String.
    def enterString(self, ctx: langParser.StringContext):
        pass

    # Exit a parse tree produced by langParser#String.
    def exitString(self, ctx: langParser.StringContext):
        pass

    # Enter a parse tree produced by langParser#Set.
    def enterSet(self, ctx: langParser.SetContext):
        pass

    # Exit a parse tree produced by langParser#Set.
    def exitSet(self, ctx: langParser.SetContext):
        pass

    # Enter a parse tree produced by langParser#Range.
    def enterRange(self, ctx: langParser.RangeContext):
        pass

    # Exit a parse tree produced by langParser#Range.
    def exitRange(self, ctx: langParser.RangeContext):
        pass

    # Enter a parse tree produced by langParser#kleeneStar.
    def enterKleeneStar(self, ctx: langParser.KleeneStarContext):
        pass

    # Exit a parse tree produced by langParser#kleeneStar.
    def exitKleeneStar(self, ctx: langParser.KleeneStarContext):
        pass

    # Enter a parse tree produced by langParser#addFinal.
    def enterAddFinal(self, ctx: langParser.AddFinalContext):
        pass

    # Exit a parse tree produced by langParser#addFinal.
    def exitAddFinal(self, ctx: langParser.AddFinalContext):
        pass

    # Enter a parse tree produced by langParser#intersect.
    def enterIntersect(self, ctx: langParser.IntersectContext):
        pass

    # Exit a parse tree produced by langParser#intersect.
    def exitIntersect(self, ctx: langParser.IntersectContext):
        pass

    # Enter a parse tree produced by langParser#in.
    def enterIn(self, ctx: langParser.InContext):
        pass

    # Exit a parse tree produced by langParser#in.
    def exitIn(self, ctx: langParser.InContext):
        pass

    # Enter a parse tree produced by langParser#vertices.
    def enterVertices(self, ctx: langParser.VerticesContext):
        pass

    # Exit a parse tree produced by langParser#vertices.
    def exitVertices(self, ctx: langParser.VerticesContext):
        pass

    # Enter a parse tree produced by langParser#unify.
    def enterUnify(self, ctx: langParser.UnifyContext):
        pass

    # Exit a parse tree produced by langParser#unify.
    def exitUnify(self, ctx: langParser.UnifyContext):
        pass

    # Enter a parse tree produced by langParser#edges.
    def enterEdges(self, ctx: langParser.EdgesContext):
        pass

    # Exit a parse tree produced by langParser#edges.
    def exitEdges(self, ctx: langParser.EdgesContext):
        pass

    # Enter a parse tree produced by langParser#setStarts.
    def enterSetStarts(self, ctx: langParser.SetStartsContext):
        pass

    # Exit a parse tree produced by langParser#setStarts.
    def exitSetStarts(self, ctx: langParser.SetStartsContext):
        pass

    # Enter a parse tree produced by langParser#smb.
    def enterSmb(self, ctx: langParser.SmbContext):
        pass

    # Exit a parse tree produced by langParser#smb.
    def exitSmb(self, ctx: langParser.SmbContext):
        pass

    # Enter a parse tree produced by langParser#setFinals.
    def enterSetFinals(self, ctx: langParser.SetFinalsContext):
        pass

    # Exit a parse tree produced by langParser#setFinals.
    def exitSetFinals(self, ctx: langParser.SetFinalsContext):
        pass

    # Enter a parse tree produced by langParser#concat.
    def enterConcat(self, ctx: langParser.ConcatContext):
        pass

    # Exit a parse tree produced by langParser#concat.
    def exitConcat(self, ctx: langParser.ConcatContext):
        pass

    # Enter a parse tree produced by langParser#valExpr.
    def enterValExpr(self, ctx: langParser.ValExprContext):
        pass

    # Exit a parse tree produced by langParser#valExpr.
    def exitValExpr(self, ctx: langParser.ValExprContext):
        pass

    # Enter a parse tree produced by langParser#reachable.
    def enterReachable(self, ctx: langParser.ReachableContext):
        pass

    # Exit a parse tree produced by langParser#reachable.
    def exitReachable(self, ctx: langParser.ReachableContext):
        pass

    # Enter a parse tree produced by langParser#brackets.
    def enterBrackets(self, ctx: langParser.BracketsContext):
        pass

    # Exit a parse tree produced by langParser#brackets.
    def exitBrackets(self, ctx: langParser.BracketsContext):
        pass

    # Enter a parse tree produced by langParser#labels.
    def enterLabels(self, ctx: langParser.LabelsContext):
        pass

    # Exit a parse tree produced by langParser#labels.
    def exitLabels(self, ctx: langParser.LabelsContext):
        pass

    # Enter a parse tree produced by langParser#filter.
    def enterFilter(self, ctx: langParser.FilterContext):
        pass

    # Exit a parse tree produced by langParser#filter.
    def exitFilter(self, ctx: langParser.FilterContext):
        pass

    # Enter a parse tree produced by langParser#varExpr.
    def enterVarExpr(self, ctx: langParser.VarExprContext):
        pass

    # Exit a parse tree produced by langParser#varExpr.
    def exitVarExpr(self, ctx: langParser.VarExprContext):
        pass

    # Enter a parse tree produced by langParser#load.
    def enterLoad(self, ctx: langParser.LoadContext):
        pass

    # Exit a parse tree produced by langParser#load.
    def exitLoad(self, ctx: langParser.LoadContext):
        pass

    # Enter a parse tree produced by langParser#finals.
    def enterFinals(self, ctx: langParser.FinalsContext):
        pass

    # Exit a parse tree produced by langParser#finals.
    def exitFinals(self, ctx: langParser.FinalsContext):
        pass

    # Enter a parse tree produced by langParser#addStarts.
    def enterAddStarts(self, ctx: langParser.AddStartsContext):
        pass

    # Exit a parse tree produced by langParser#addStarts.
    def exitAddStarts(self, ctx: langParser.AddStartsContext):
        pass

    # Enter a parse tree produced by langParser#starts.
    def enterStarts(self, ctx: langParser.StartsContext):
        pass

    # Exit a parse tree produced by langParser#starts.
    def exitStarts(self, ctx: langParser.StartsContext):
        pass

    # Enter a parse tree produced by langParser#map.
    def enterMap(self, ctx: langParser.MapContext):
        pass

    # Exit a parse tree produced by langParser#map.
    def exitMap(self, ctx: langParser.MapContext):
        pass


del langParser
