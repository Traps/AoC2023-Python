import util

DAY_NUM: int = 1

def evaluate_line(line:str) -> int:
    v0 = next(ord(c)-48 for c in line if c.isnumeric())
    v1 = next(ord(c)-48 for c in reversed(line) if c.isnumeric())

    return v0 * 10 + v1


def solve(_input: str) -> int:
    return sum(evaluate_line(line) for line in _input.splitlines())


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
