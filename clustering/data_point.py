from __future__ import annotations
from typing import Iterator, Tuple, List, Iterable
from math import sqrt

class DataPoint:
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = Tuple(initial)
        self.dimensions: Tuple[float, ...] = Tuple(initial)

    @property
    def num_dimensions(self) -> int:
        return len(self.dimensions)
    
    