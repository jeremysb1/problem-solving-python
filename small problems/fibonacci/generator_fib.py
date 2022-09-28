from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 #special case
    if n > 1: yield 1 #special case
    last: int = 0 
    next: int = 1
    for _ in range(1, n): 
        last, next = next, last + next
        yield next # main generstion step

if __name__ == "__main__":
    for i in fib6(50):
        print(i)
