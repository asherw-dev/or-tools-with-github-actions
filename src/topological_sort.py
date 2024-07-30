from typing import List
from ortools.sat.python import cp_model
from graph import Graph, Node

def validate_topological_sort(graph: Graph, sort: List[Node]) -> bool:
    position = {node: idx for idx, node in enumerate(sort)}
    for node in graph.nodes:
        for target in graph.out_nodes(node):
            if position[node] >= position[target]:
                return False
    return True

def find_topological_sort(graph: Graph) -> List[Node]:
    model = cp_model.CpModel()
    node_vars = {node: model.NewIntVar(0, len(graph.nodes) - 1, f'node_{node.id}') for node in graph.nodes}

    for node in graph.nodes:
        for target in graph.out_nodes(node):
            model.Add(node_vars[node] < node_vars[target])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        sorted_nodes = sorted(graph.nodes, key=lambda node: solver.Value(node_vars[node]))
        return sorted_nodes
    else:
        return []
