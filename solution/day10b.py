import shapely

from typing import Iterator

import util

from solution.day10a import parse_pipes

DAY_NUM: int = 10

def generate_path(start_node:tuple, connections:dict) -> Iterator[tuple[int, int]]:
    last_node = next_node = None
    current_node = start_node

    while next_node != start_node:
        yield (next_node := next(n for n in connections[current_node] if n != last_node))

        last_node = current_node
        current_node = next_node


def solve(_input:str) -> int:
    start_pos, connections = parse_pipes(_input)

    interior = shapely.Polygon(generate_path(start_pos, connections))

    enclosed_tiles = shapely.buffer(interior, -0.5, join_style='mitre')
    
    return int(round(enclosed_tiles.area))

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(10))}')
