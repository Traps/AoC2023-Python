from typing import Iterable

import util

from solution.day13a import fold_at

DAY_NUM: int = 13

def distance(item0:str, item1:str) -> int:
    return sum(c0!=c1 for c0,c1 in zip(item0, item1)) 


def find_mirror_point(items:Iterable[str]) -> int:
    items = tuple(items)

    for i in range(1, len(items)):
        if sum(distance(s0, s1) for s0,s1 in fold_at(items, i)) == 1:
            return i


def evaluate_pattern(pattern:str) -> int:
    rows = pattern.splitlines()

    return find_mirror_point(zip(*rows)) or find_mirror_point(rows)*100
 

def solve(_input: str) -> int:
    patterns = _input.split('\n\n')

    return sum(evaluate_pattern(pattern) for pattern in patterns)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
