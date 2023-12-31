import collections
import dataclasses

from typing import Final, Iterator

import util
from solution.day16a import Vec2

DAY_NUM: Final[int] = 17

@dataclasses.dataclass(slots=True, eq=True, frozen=True)
class Crucible(object):
    position: Vec2
    previous_moves: int

    def available_moves(self):
        last_move = self.previous_moves & 0b11

        yield last_move ^ 1
        yield last_move ^ 3

        if self.previous_moves not in (0b000000, 0b010101, 0b101010, 0b111111):
            yield last_move

    def move(self, direction:int) -> 'Crucible':
        step = (Vec2(1,0), Vec2(0,-1), Vec2(-1,0), Vec2(0,1))[direction]

        return Crucible(self.position+step, (self.previous_moves<<2) + direction & 0b111111)
    
    def move_options(self) -> Iterator['Crucible']:
        for dir in self.available_moves():
            yield self.move(dir)

    def in_bounds(self, city_size:Vec2) -> bool:
        return 0 <= self.position.x <= city_size.x and 0 <= self.position.y <= city_size.y
    
    @staticmethod
    def make_start(start_pos:Vec2) -> list[tuple[int, 'Crucible']]:
        return [(0, Crucible(start_pos, dir)) for dir in (0, 2)]


def parse_map(_input:str) -> tuple:
    return {Vec2(i, j):int(v) for j,line in enumerate(_input.splitlines())
                             for i,v in enumerate(line)}


def minimize_path(start_pos:Vec2, goal_pos:Vec2, cost_map:dict) -> int:
    city_size = Vec2(max(v.x for v in cost_map), max(v.y for v in cost_map))

    shortest_path_guess = sum(d for p,d in cost_map.items()
                                if p.x==p.y or p.x==(p.y+1))
    
    distance_map = collections.defaultdict(lambda: shortest_path_guess)

    to_visit = Crucible.make_start(start_pos)
    
    for distance, crucible in to_visit:
        distance_map[crucible] = distance
    
    while to_visit:
        to_visit = sorted(to_visit, key=lambda p: p[0], reverse=True)
        
        distance, crucible = to_visit.pop()

        for candidate in crucible.move_options():
            if not candidate.in_bounds(city_size):
                continue
            
            candidate_distance = distance + cost_map[candidate.position]
            if candidate_distance > shortest_path_guess:
                continue

            if distance_map[candidate] > candidate_distance:
                distance_map[candidate] = candidate_distance

                to_visit.append((candidate_distance, candidate))

                if candidate.position == goal_pos:
                    return candidate_distance


def solve(_input: str) -> int:
    cost_map = parse_map(_input)
    start_pos = Vec2(0,0)
    goal_pos = Vec2(max(v.x for v in cost_map),
                    max(v.y for v in cost_map))
    
    return minimize_path(start_pos, goal_pos, cost_map)


if __name__ == '__main__':
    # from timeit import timeit
    # _input = util.get_sample(DAY_NUM)
    # print(timeit('solve(_input)', number=1, globals={'solve':solve, '_input':_input}))
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_sample(DAY_NUM))}')
