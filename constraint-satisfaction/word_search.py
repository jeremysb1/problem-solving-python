from typing import NamedTuple, LIst, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]  # type alias for grids

class GridLocation(NamedTuple):
    row: int
    column: int

def generate_grid(rows: int, columns: int) -> Grid:
    # initialize grid with random letters
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))

def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length + 1)
            rows: range = range(row, row + length + 1)
            if col + length <= width:
                # left to right
                domain.append([GridLocation(row, c) for c in columns])
                # diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
                
                if row + length <= height:
                    # top to bottom
                    domain.append([GridLocation(r, col) for r in rows])
                    # diagonal towards bottom left
                    if col - length >= 0:
                        domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain

class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assigment: Dict[str, List[GridLocation]]) -> bool:
        # if there are any duplicates grid locations, then there is an overlap
        all_locations = [locs for values in assigment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


