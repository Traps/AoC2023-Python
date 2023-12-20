from typing import Iterable

import util

DAY_NUM: int = 13


def fold_at(items:Iterable[str], pos:int) -> Iterable[tuple[str, str]]:
    return zip(items[pos-1::-1], items[pos::])


def find_mirror_point(items:Iterable[any]) -> int|None:
    items = tuple(hash(item) for item in items)

    for i in range(1, len(items)):
        if all(v0==v1 for v0,v1 in fold_at(items, i)):
            return i
        
    return None


def evalaute_pattern(pattern:str) -> int:
    rows = pattern.splitlines()

    return find_mirror_point(zip(*rows)) or find_mirror_point(rows)*100


def solve(_input: str) -> int:
    patterns = _input.split('\n\n')

    return sum(evalaute_pattern(pattern) for pattern in patterns)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
