import dataclasses
import itertools
import shapely

from typing import Final

import util

DAY_NUM: Final[int] = 18


@dataclasses.dataclass(slots=True, eq=True, frozen=True)
class Vec2(object):
    x: int
    y: int

    @property
    def xy(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __add__(self, other) -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __mul__(self, factor) -> 'Vec2':
        return Vec2(self.x * factor, self.y * factor)


DIRECTIONS: Final[dict] = {'R':Vec2(1,0), 'D':Vec2(0,-1), 'L':Vec2(-1,0), 'U':Vec2(0,1)}


def parse_instruction(line:str) -> Vec2:
    direction, step_count, _ = line.split()

    direction = DIRECTIONS[direction]
    step_count = int(step_count)

    return direction * step_count

def excavate_lagoon(instructions:list) -> shapely.Polygon:
    nodes = itertools.accumulate([Vec2(0,0), *instructions])

    trench = shapely.LineString(n.xy for n in nodes).buffer(0.5, join_style='mitre')

    boundaries = shapely.get_parts(trench.boundary)
    
    return shapely.union_all([shapely.Polygon(b) for b in boundaries])


def solve(_input: str) -> int:
    instructions = [parse_instruction(line) for line in _input.splitlines()]

    lagoon = excavate_lagoon(instructions)

    return int(lagoon.area)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
