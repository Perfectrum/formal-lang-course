# Generated from lang.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
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

    # Enter a parse tree produced by langParser#val.
    def enterVal(self, ctx: langParser.ValContext):
        pass

    # Exit a parse tree produced by langParser#val.
    def exitVal(self, ctx: langParser.ValContext):
        pass

    # Enter a parse tree produced by langParser#expr.
    def enterExpr(self, ctx: langParser.ExprContext):
        pass

    # Exit a parse tree produced by langParser#expr.
    def exitExpr(self, ctx: langParser.ExprContext):
        pass


del langParser
