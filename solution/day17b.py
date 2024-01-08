from typing import Final

import util
from solution.day16a import Vec2
from solution.day17a import minimize_path, parse_map


DAY_NUM: Final[int] = 17


def solve(_input: str) -> int:
    cost_map = parse_map(_input)
    start_pos = Vec2(0, 0)
    goal_pos = Vec2(max(v.x for v in cost_map), max(v.y for v in cost_map))
    
    return minimize_path(start_pos, goal_pos, cost_map, range(3, 10))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
