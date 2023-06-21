from dataclasses import dataclass

from ..fa_utils import graph2nfa
from ..graph_regular_query import get_reachable_vertices


@dataclass
class Graph:
    graph: None
    starts = set()
    finals = set()

    def get_edges(self):
        return self.graph.edges()

    def get_vertices(self):
        return set(self.graph.nodes())

    def get_labels(self):
        labels = set(map(lambda edge: edge[2], self.graph.edges(data="labels")))
        if labels == {None}:
            return set()

    def get_reachable(self):
        return get_reachable_vertices(
            graph2nfa(self.graph),
            self.graph,
            self.starts,
        )

    def set_starts(self, starts):
        if isinstance(starts, int):
            self.starts = {starts}
        else:
            self.starts = starts

    def set_finals(self, finals):
        if isinstance(finals, int):
            self.finals = {finals}
        else:
            self.finals = finals

    def add_start(self, npde):
        self.starts.add(node)

    def add_final(self, npde):
        self.finals.add(node)
