import util

DAY_NUM: int = 9

from solution.day09a import diff


def extrapolate_left(values:tuple[int]) -> int:
    if all(v==0 for v in values):
        return 0
    
    return values[0] - extrapolate_left(diff(values))


def solve(_input: str) -> int:
    histories = [tuple(int(v) for v in line.split()) for line in _input.splitlines()]
    
    return sum(extrapolate_left(history) for history in histories)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
