from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Terminal
from scipy.sparse import dok_matrix, csr_matrix

from project.cfg_utils import cfg2wcnf
from project.cfg_utils import from_file


def matrix(graph: MultiDiGraph, cfg: CFG):
    """
    Perform matrix reachability algorithm

    Args:
        graph: graph (any type from networkx.Graph)
        cfg: context free grammar as file or pyformlang CFG

    Returns:
        set of triplet tuples of starting graph node, CFG variable, final achievable graph node
    """
    if not isinstance(cfg, CFG):
        cfg = from_file(cfg)
    cfg = cfg2wcnf(cfg)

    matrices = {}
    for var in cfg.variables:
        matrices[var] = dok_matrix((graph.number_of_nodes(), graph.number_of_nodes()))

    for prod in cfg.productions:
        matrix = matrices[prod.head]

        if len(prod.body) == 0:
            for i in range(graph.number_of_nodes()):
                matrix[i, i] = 1

        if len(prod.body) == 1:
            if isinstance(prod.body[0], Terminal):
                prod.body[0] = prod.body[0].value

                for (u, v, label) in graph.edges(data="label"):
                    if label == prod.body[0]:
                        matrix[u, v] = 1

    matrices = {var: m.tocsr() for var, m in matrices.items()}

    while True:
        new_matrices = {
            var: csr_matrix((graph.number_of_nodes(), graph.number_of_nodes()))
            for var in cfg.variables
        }

        for prod in cfg.productions:
            if len(prod.body) == 2:
                new_matrices[prod.head] += (
                    matrices[prod.body[0]] @ matrices[prod.body[1]]
                )

        nonzeros = {var: m.count_nonzero() for var, m in matrices.items()}

        for var, m in new_matrices.items():
            matrices[var] += m

        if {var: m.count_nonzero() for var, m in matrices.items()} == nonzeros:
            break

    res = set()
    for var, m in matrices.items():
        m = m.tocoo()

        for i, j, v in zip(m.row, m.col, m.data):
            if v:
                res.add((i, var, j))

    return res
