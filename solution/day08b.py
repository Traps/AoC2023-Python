import itertools
import math

from typing import Iterator

import util
from solution.day08a import parse_network

DAY_NUM: int = 8

def iter_path(turns:str, network:dict, start_node:str) -> Iterator[str]:    
    yield (current_node := start_node)

    for turn in itertools.cycle(turns):
        yield (current_node := network[(current_node, turn)])
    

def solve(_input: str) -> int:
    turns, nodes = _input.split('\n\n')

    network = parse_network(nodes)

    start_nodes = {node for node, turn in network if node.endswith('A')}

    iter_from = lambda start: enumerate(iter_path(turns, network, start))

    exit_interval = [next(i for i,n in iter_from(start_node) if n.endswith('Z'))
                        for start_node in start_nodes]
    
    return math.lcm(*exit_interval)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
