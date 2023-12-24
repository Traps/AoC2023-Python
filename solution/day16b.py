from typing import Iterator

import util

from solution.day16a import make_cached_beam_function, count_lit_tiles, Beam, Vec2


DAY_NUM: int = 16


def generate_start_beams(_input:str) -> Iterator[Beam]:
    board_size = Vec2(_input.index('\n'), _input.count('\n') + 1)

    for x in range(0, board_size.x):
        yield Beam(Vec2(x, 0), Vec2(0, 1))
        yield Beam(Vec2(x, board_size.y - 1), Vec2(0, -1))

    for y in range(0, board_size.y):
        yield Beam(Vec2(0, y), Vec2(1, 0))
        yield Beam(Vec2(board_size.x -1, y), Vec2(-1, 0))


def solve(_input: str) -> int:
    extrapolate_beam = make_cached_beam_function(_input)
    start_beams = generate_start_beams(_input)

    return max(count_lit_tiles(beam, extrapolate_beam) for beam in start_beams)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')

    