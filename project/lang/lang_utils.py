import sys
import os

from antlr4 import *
from pydot import *

from project.lang.antlrgen.langLexer import langLexer
from project.lang.antlrgen.langParser import langParser
from project.lang.listener import Listener


def check_syntax(code=None):
    if not code:
        stream = FileStream(sys.argv[1])

    if os.path.exists(code):
        stream = FileStream(code)

    stream = InputStream(code)
    parser = langParser(CommonTokenStream(langLexer(stream)))
    tree = parser.prog()
    return parser.getNumberOfSyntaxErrors() == 0


def code2dot(code, filename=None):
    if not code:
        stream = FileStream(sys.argv[1])

    if os.path.exists(code):
        stream = FileStream(code)
    else:
        stream = InputStream(code)

    listener = Listener()
    ParseTreeWalker().walk(
        listener, langParser(CommonTokenStream(langLexer(stream))).prog()
    )

    if filename:
        listener.dot.write(filename)
    return listener.dot.to_string()
