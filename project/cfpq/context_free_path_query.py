from typing import List, Callable

from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable


def context_free_path_query(
    algo: Callable,
    graph: MultiDiGraph,
    cfg: CFG,
    start_states: List[any] = None,
    final_states: List[any] = None,
    nonterm: Variable = None,
):
    """
    Queries given graph reachability problem for a given set of start and end ndoes,
    and a given nonterminal using given algorithm

    Args:
        algo: algorithm to use (hellings or matrix)
        graph: the graph to query
        cfg: context-free grammar
        start_states: start nodes of the given graph
        final_states: final nodes of the given graph
        nonterm: nonterminal

    Returns:
        set of node pairs
    """
    if start_states is None:
        start_states = set(graph.nodes)

    if final_states is None:
        final_states = set(graph.nodes)

    if nonterm is None:
        nonterm = cfg.start_symbol

    return {
        (v, u)
        for v, n, u in algo(graph, cfg)
        if n == nonterm and v in start_states and u in final_states
    }
