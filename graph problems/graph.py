from modulefinder import EXTENDED_ARG
from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')  # type of the vertices in the graph

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
