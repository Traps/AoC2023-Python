from typing import Final

import util
from solution.day18a import Vec2, DIRECTIONS
from solution.day18a import excavate_lagoon

DAY_NUM: Final[int] = 18


def parse_instruction(line:str) -> Vec2:
    *_, color = line.split()

    direction = DIRECTIONS['RDLU'[int(color[-2])]]
    step_count = int(color[2:-2], base=16)

    return direction * step_count


def solve(_input: str) -> int:
    instructions = [parse_instruction(line) for line in _input.splitlines()]

    lagoon = excavate_lagoon(instructions)

    return int(lagoon.area)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
