import itertools

import util

DAY_NUM: int = 9

def diff(values:tuple[int]) -> tuple[int]:
    return tuple(v1-v0 for v0,v1 in itertools.pairwise(values))


def extrapolate(values:tuple[int]) -> int:
    if all(v==0 for v in values):
        return 0
    
    return values[-1] + extrapolate(diff(values))


def solve(_input: str) -> int:
    histories = [tuple(int(v) for v in line.split()) for line in _input.splitlines()]
    
    return sum(extrapolate(history) for history in histories)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
