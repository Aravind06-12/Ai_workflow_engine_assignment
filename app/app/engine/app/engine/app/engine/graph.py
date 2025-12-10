# app/engine/graph.py
from typing import Dict, Callable, Optional
from dataclasses import dataclass

@dataclass
class Graph:
    graph_id: str
    nodes: Dict[str, Callable]
    edges: Dict[str, str]
    start: str

    def get_node(self, name: str):
        return self.nodes.get(name)

    def next_from_edge(self, name: str) -> Optional[str]:
        return self.edges.get(name)
