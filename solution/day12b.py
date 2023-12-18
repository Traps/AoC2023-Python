import util

from solution.day12a import count_arrangements

DAY_NUM: int = 12


def solve(_input: str) -> int:
    rows, groups = zip(*(line.split(' ') for line in _input.splitlines()))

    rows = ('?'.join(row for _ in range(5)) for row in rows)
    groups = (tuple(int(v) for v in group.split(',')) * 5 for group in groups)
    
    return sum(count_arrangements(row, group) for row,group in zip(rows, groups))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
