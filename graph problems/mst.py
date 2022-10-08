from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')  # type of the vertices in the graph
WeightedPath = List[WeightedEdge]

def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])