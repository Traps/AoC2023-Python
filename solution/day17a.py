import bisect
import dataclasses

from typing import Final, Iterator

import util
from solution.day16a import Vec2


DAY_NUM: Final[int] = 17


@dataclasses.dataclass(slots=True, eq=True, frozen=True, repr=False)
class Crucible(object):
    position: Vec2
    last_move: int
    heat_loss: int = dataclasses.field(hash=False, compare=False)

    def in_bounds(self, city_size:Vec2) -> bool:
        return (0 <= self.position.x <= city_size.x 
                and 0 <= self.position.y <= city_size.y)

    def move_options(self, cost_map:dict, move_range:range) -> Iterator['Crucible']:
        for direction in (self.last_move ^ 1, self.last_move ^ 3):
            step = (Vec2(1,0), Vec2(0,-1), Vec2(-1,0), Vec2(0,1))[direction]
            
            heat_loss = self.heat_loss
            position = self.position

            for i_move in range(move_range.stop):
                position += step
                if position not in cost_map:
                    break

                heat_loss += cost_map[position]

                if i_move >= move_range.start:
                    yield Crucible(position, direction, heat_loss)
        
    @staticmethod
    def make_start(start_pos:Vec2) -> list[tuple[int, 'Crucible']]:
        return [Crucible(start_pos, dir, 0) for dir in (0, 1)]
    
    
def parse_map(_input:str) -> tuple:
    return {Vec2(i, j):int(v) for j, line in enumerate(_input.splitlines())
                              for i, v in enumerate(line)}


def minimize_path(start_pos:Vec2, goal_pos:Vec2, cost_map:dict, move_range:range) -> int:
    worst_guess = sum(cost_map.values())

    to_visit = Crucible.make_start(start_pos)
    
    distance_map = {crucible:crucible.heat_loss for crucible in to_visit}
    
    while to_visit:
        crucible = to_visit.pop(0)
        
        if crucible.position == goal_pos:
            return crucible.heat_loss

        for candidate in crucible.move_options(cost_map, move_range):
            if candidate.heat_loss >= distance_map.get(candidate, worst_guess):
                continue
                
            distance_map[candidate] = candidate.heat_loss

            bisect.insort(to_visit, candidate, key=lambda c: c.heat_loss)
            

def solve(_input: str) -> int:
    cost_map = parse_map(_input)
    start_pos = Vec2(0, 0)
    goal_pos = Vec2(max(v.x for v in cost_map), max(v.y for v in cost_map))
    
    return minimize_path(start_pos, goal_pos, cost_map, range(0,3))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
