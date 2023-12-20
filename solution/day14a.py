import util

DAY_NUM: int = 14

def settle_rocks(column:str) -> str:
    if '.O' in column:
        return settle_rocks(column.replace('.O', 'O.'))

    return column


def calculate_load(column:str) -> int:
    return sum((c=='O') * i for i,c in enumerate(reversed(column), 1))


def solve(_input: str) -> int:
    columns = (''.join(col) for col in zip(*_input.splitlines()))
    columns = (settle_rocks(col) for col in columns)

    return sum(calculate_load(col) for col in columns)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
