import dataclasses
import functools

import util

DAY_NUM: int = 16


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
    
    def propagate(self, obstacle:str) -> 'Beam':
        match self.vel, obstacle:
            case _, None:
                return (Beam(self.pos + self.vel, self.vel),)
            case Vec2(x=1|-1), '/':
                return (self.rot90(1),)
            case Vec2(x=1|-1), '\\':
                return (self.rot90(-1),)
            case Vec2(y=1|-1), '/':
                return (self.rot90(-1),)
            case Vec2(y=1|-1), '\\':
                return (self.rot90(1),)
            case Vec2(x=1|-1), '|':
                return (self.rot90(1), self.rot90(-1))
            case Vec2(y=1|-1), '-':
                return (self.rot90(1), self.rot90(-1))
        
        return (Beam(self.pos + self.vel, self.vel),)
    
    def rot90(self, ccw_steps:int) -> 'Beam':
        directions = (Vec2(1,0), Vec2(0,-1), Vec2(-1,0), Vec2(0,1))

        new_direction = directions[(directions.index(self.vel) + ccw_steps) % 4]

        return Beam(self.pos + new_direction, new_direction)
    

def parse_obstacles(_input:str) -> dict:
    obstacles = {}
    for j,line in enumerate(_input.splitlines()):
        obstacles |= {Vec2(i,j):obs for i,obs in enumerate(line) if obs!='.'}

    return obstacles


def get_energized_count(obstacles:dict, x_range:range, y_range:range, start_beam:Beam) -> int:
    visited = set()
    to_visit = [start_beam]

    while to_visit:
        beam = to_visit.pop()
        visited.add(beam)

        for new_beam in beam.propagate(obstacles.get(beam.pos, None)):
            if new_beam not in visited and new_beam.pos.x in x_range and new_beam.pos.y in y_range:
                to_visit.append(new_beam)

    return len(set(beam.pos for beam in visited))


def solve(_input: str) -> int:
    x_range = range(0, _input.index('\n'))
    y_range = range(0, _input.count('\n') + 1)
    
    obstacles = parse_obstacles(_input)
    
    return get_energized_count(obstacles, x_range, y_range, Beam(Vec2(0,0), Vec2(1,0)))

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
