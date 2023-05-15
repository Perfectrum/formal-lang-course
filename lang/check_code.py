import sys
from antlr4 import *
from langLexer import langLexer
from langParser import langParser

if __name__ == "__main__":
    input_stream = FileStream(sys.argv[1])
    lexer = langLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = langParser(token_stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() == 0:
        print("Code is correct")
