from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V')  # type of the vertices in the graph

class WeightedGraph(Generic[V], Graph[V]):
    