import sys
import argparse
from antlr4 import *


if "." in __name__:
    from .antlrgen.langParser import langParser
    from .antlrgen.langLexer import langLexer
    from .antlrgen.langVisitor import langVisitor
    from .visitor import Visitor
else:
    from antlrgen.langParser import langParser
    from antlrgen.langLexer import langLexer
    from antlrgen.langVisitor import langVisitor
    from visitor import Visitor


class Interpreter:
    def interpret(self, source: str, stream=None):
        lexems = langLexer(InputStream(source))
        parser = langParser(CommonTokenStream(lexems))

        tree = parser.prog()
        visitor = Visitor(stream)

        error = visitor.visit(tree)
        if isinstance(error, str):
            return error
        return None


if __name__ == "__main__":
    interpreter = Interpreter()
    argparser = argparse.ArgumentParser(description="Interpreter CLI")
    argparser.add_argument("filename", nargs="?", help="file to run")
    args = argparser.parse_args()

    if args.filename:
        with open(args.filename, "r") as source_file:
            interpreter.interpret(source_file.read())
    else:
        while True:
            code = input("╰( ⁰ o ⁰)━☆ﾟ.*･｡ﾟ ")
            if code == "exit":
                break
            interpreter.interpret(code)
