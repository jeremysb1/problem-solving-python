from __future__ import annotations
from typing import NewType, List
from abc import ABC, abstractmethod

Move = NewType('Move', int)

class Piece:
    @property
    def opposite(self) -> Piece:
        raise NotImplementedError("Should be implemented by subclasses.")