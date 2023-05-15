from antlr4 import *
from pydot import *

from project.lang.antlrgen.langLexer import langLexer
from project.lang.antlrgen.langParser import langParser
from project.lang.antlrgen.langListener import langListener


class Listener(langListener):
    def __init__(self):
        super().__init__()

        self.nodes = {}
        self.num_nodes = 0
        self.rules = langParser.ruleNames
        self.dot = Dot("tree", graph_type="digraph")

    def visitTerminal(self, node):
        self.dot.add_edge(Edge(self.nodes[node.parentCtx], self.num_nodes))

        self.dot.add_node(Node(self.num_nodes, label=node.getText()))

        self.num_nodes += 1

    def enterEveryRule(self, ctx):
        if ctx not in self.nodes:
            self.nodes[ctx] = self.num_nodes
            self.num_nodes += 1

        if ctx.parentCtx:
            self.dot.add_edge(Edge(self.nodes[ctx.parentCtx], self.nodes[ctx]))

        self.dot.add_node(Node(self.nodes[ctx], label=self.rules[ctx.getRuleIndex()]))
