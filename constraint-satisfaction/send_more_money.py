from csp import Constraint, CSP
from typing import Dict, List, Optional

class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assigment: Dict[str, int]) -> bool:
        # if there are duplicate values, then it's not a solution
        if len(set(assigment.values())) < len(assigment):
            return False

        # if all variables have been assigned, check if it adds correctly
        if len(assigment) == len(self.letters):
            s: int = assigment["S"]
            e: int = assigment["E"]
            n: int = assigment["N"]
            d: int = assigment["D"]
            m: int = assigment["M"]
            o: int = assigment["O"]
            r: int = assigment["R"]
            y: int = assigment["Y"]
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True  # no conflict

