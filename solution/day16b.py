import functools
import itertools

import util

from solution.day16a import parse_obstacles, get_energized_count, Beam, Vec2


DAY_NUM: int = 16


def solve(_input: str) -> int:
    x_range = range(0, _input.index('\n'))
    y_range = range(0, _input.count('\n') + 1)
    
    obstacles = parse_obstacles(_input)
    
    start_beams = itertools.chain(
            (Beam(Vec2(0, y), Vec2(1, 0)) for y in y_range),
            (Beam(Vec2(x_range.stop - 1, y), Vec2(-1, 0)) for y in y_range),
            (Beam(Vec2(x, 0), Vec2(0, 1)) for x in x_range),
            (Beam(Vec2(x, y_range.stop - 1), Vec2(0, -1)) for x in x_range)
        )

    evaluate_start = functools.partial(
            get_energized_count, 
            obstacles=obstacles, 
            x_range=x_range, 
            y_range=y_range
        )

    return max(evaluate_start(start_beam=beam) for beam in start_beams)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
