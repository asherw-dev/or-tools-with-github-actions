from dataclasses import dataclass
from typing import Set, List, Dict

@dataclass(frozen=True)
class Node:
    id: str

@dataclass(frozen=True)
class Edge:
    source: Node
    target: Node

class Graph:
    def __init__(self):
        self.nodes: Set[Node] = set()
        self.edges: Set[Edge] = set()
        self.adj_list: Dict[Node, Set[Node]] = {}
        self.rev_adj_list: Dict[Node, Set[Node]] = {}

    def add_edge(self, source: Node, target: Node):
        edge = Edge(source, target)
        self.nodes.update([source, target])
        self.edges.add(edge)
        if source not in self.adj_list:
            self.adj_list[source] = set()
        if target not in self.rev_adj_list:
            self.rev_adj_list[target] = set()
        self.adj_list[source].add(target)
        self.rev_adj_list[target].add(source)

    def in_edges(self, node: Node) -> Set[Edge]:
        return {edge for edge in self.edges if edge.target == node}

    def out_edges(self, node: Node) -> Set[Edge]:
        return {edge for edge in self.edges if edge.source == node}

    def sources(self) -> Set[Node]:
        return {node for node in self.nodes if not self.rev_adj_list.get(node)}

    def sinks(self) -> Set[Node]:
        return {node for node in self.nodes if not self.adj_list.get(node)}

    def in_nodes(self, node: Node) -> Set[Node]:
        return self.rev_adj_list.get(node, set())

    def out_nodes(self, node: Node) -> Set[Node]:
        return self.adj_list.get(node, set())

    def to_string(self) -> str:
        return ';'.join(f"{edge.source.id}->{edge.target.id}" for edge in self.edges)

    @staticmethod
    def from_string(graph_str: str) -> 'Graph':
        graph = Graph()
        for edge_str in graph_str.split(';'):
            if '->' in edge_str:
                source_id, target_id = edge_str.split('->')
                source = Node(source_id)
                target = Node(target_id)
                graph.add_edge(source, target)
        return graph
