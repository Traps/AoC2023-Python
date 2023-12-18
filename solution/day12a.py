import functools

import util

DAY_NUM: int = 12


@functools.cache
def count_arrangements(row:str, groups:tuple[int]) -> int:
    if not groups:
        return '#' not in row

    row = row.lstrip('.')

    damaged_tot = sum(groups)
    if damaged_tot > sum(1 for c in row if c != '.') or damaged_tot + len(groups) - 1 > len(row):
        return 0
    
    arrangements = 0 if row[0] != '?' else count_arrangements(row[1:], groups)
    
    n_damaged = groups[0]

    if '.' not in row[:n_damaged] and (len(row) == n_damaged or row[n_damaged] != '#'):
        return arrangements + count_arrangements(row[n_damaged+1:], groups[1:])

    return arrangements

    
def solve(_input: str) -> int:
    rows, groups = zip(*(line.split(' ') for line in _input.splitlines()))

    groups = (tuple(int(v) for v in group.split(',')) for group in groups)
    
    return sum(count_arrangements(row, group) for row,group in zip(rows, groups))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
