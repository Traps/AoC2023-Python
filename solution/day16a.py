import dataclasses
import functools
from typing import Callable, Final

import util

DAY_NUM: Final[int] = 16


@dataclasses.dataclass(slots=True, eq=True, frozen=True)
class Vec2(object):
    x: int
    y: int

    def __add__(self, other) -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)


@dataclasses.dataclass(slots=True, eq=True, frozen=True)
class Beam(object):
    pos: Vec2
    vel: Vec2

    def step(self) -> 'Beam':
        return Beam(self.pos + self.vel, self.vel)
    
    def rot90(self, ccw_steps:int) -> 'Beam':
        directions = (Vec2(1,0), Vec2(0,-1), Vec2(-1,0), Vec2(0,1))

        new_direction = directions[(directions.index(self.vel) + ccw_steps) % 4]

        return Beam(self.pos + new_direction, new_direction)
    
    def in_bounds(self, board_size:Vec2) -> bool:
        return 0 <= self.pos.x < board_size.x and 0 <= self.pos.y < board_size.y


def make_cached_beam_function(_input:str) -> \
        Callable[[Beam], tuple[set[Beam], tuple[Beam, ...]]]:
   
    OBSTACLES: Final[dict] = {}
    for j,line in enumerate(_input.splitlines()):
        OBSTACLES |= {Vec2(i,j):obs for i,obs in enumerate(line) if obs!='.'}

    BOARD_SIZE: Final[Vec2] = Vec2(_input.index('\n'), _input.count('\n') + 1)
    
    @functools.cache
    def update_beam(beam:Beam) -> Beam:
        match OBSTACLES.get(beam.pos, None), beam.vel:
            case None, _:
                return (beam.step(),)
            case '/', Vec2(x=1|-1):
                return (beam.rot90(1),)
            case '\\', Vec2(x=1|-1):
                return (beam.rot90(-1),)
            case '/', Vec2(y=1|-1):
                return (beam.rot90(-1),)
            case '\\', Vec2(y=1|-1):
                return (beam.rot90(1),)
            case '|', Vec2(x=1|-1):
                return (beam.rot90(1), beam.rot90(-1))
            case '-', Vec2(y=1|-1):
                return (beam.rot90(1), beam.rot90(-1))
        
        return (beam.step(),)
    
    @functools.cache
    def extrapolate_beam(beam:Beam) -> tuple[set[Beam], tuple[Beam, ...]]:
        if not beam.in_bounds(BOARD_SIZE):
            return (tuple(), tuple())
        
        visited = set()
        to_visit = (beam,)

        while len(to_visit) == 1 and to_visit[0] not in visited:
            visited.add(to_visit[0])

            to_visit = tuple(bm for bm in update_beam(to_visit[0])
                                if bm.in_bounds(BOARD_SIZE))

        return visited, to_visit

    return extrapolate_beam


def count_lit_tiles(start_beam:Beam, extrapolate_beam:callable) -> int:
    visited = set()
    to_visit = [start_beam]
    
    while to_visit:
        passed_by, new_to_visit = extrapolate_beam(to_visit.pop())
        
        visited |= passed_by

        for new_beam in new_to_visit:
            if new_beam not in visited:
                to_visit.append(new_beam)

    return len(set(beam.pos for beam in visited))


def solve(_input: str) -> int:
    extrapolate_beam = make_cached_beam_function(_input)
    start_beam = Beam(Vec2(0,0), Vec2(1,0))

    return count_lit_tiles(start_beam, extrapolate_beam)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
