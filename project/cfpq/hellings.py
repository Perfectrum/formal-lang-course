from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable

from project.cfg_utils import cfg2wcnf, from_file


def hellings(graph: MultiDiGraph, cfg: CFG):
    """
    Perform Hellings reachability algorithm

    Args:
        graph: graph (any type from networkx.Graph)
        cfg: context free grammar as file or pyformlang CFG

    Returns:
        set of triplet tuples of starting graph node, CFG variable, final achievable graph node
    """

    if not isinstance(cfg, CFG):
        cfg = from_file(cfg)

    cfg = cfg2wcnf(cfg)

    res = set()

    for prod in cfg.productions:
        if len(prod.body) == 0:
            [res.add((node, prod.head, node)) for node in graph.nodes]
        elif len(prod.body) == 1:
            [
                res.add((u, prod.head, v))
                for u, v, label in graph.edges.data(data="label")
                if Variable(label) == prod.body[0]
            ]

    queue = list(res)

    while len(queue) > 0:
        u1, var1, v1 = queue.pop()

        next_res = set()

        for u2, var2, v2 in res:
            if v2 != u1:
                continue

            for prod in cfg.productions:
                if prod.body == [var2, var1] and (u2, prod.head, v1) not in res:
                    next_res.add((u2, prod.head, v1))

        for v2, var2, u2 in res:
            if v2 != v1:
                continue

            for prod in cfg.productions:
                if prod.body == [var1, var2] and (u1, prod.head, u2) not in res:
                    next_res.add((u1, prod.head, u2))

        [res.add(t) for t in next_res]
        [queue.append(t) for t in next_res]

    return res
