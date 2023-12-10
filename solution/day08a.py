import itertools
import re

from typing import Iterator

import util

DAY_NUM: int = 8

def iter_path(turns:str, network:dict) -> Iterator[str]:    
    yield (current_node := 'AAA')

    for turn in itertools.cycle(turns):
        yield (current_node := network[(current_node, turn)])
    

def parse_network(nodes:str) -> dict[tuple[str, str], str]:
    network = {}

    for line in nodes.splitlines():
        src, left, right = re.findall(r'\w{3}', line)

        network[(src, 'L')] = left
        network[(src, 'R')] = right

    return network


def solve(_input: str) -> int:
    turns, nodes = _input.split('\n\n')

    path = iter_path(turns, parse_network(nodes))

    return sum(1 for _ in itertools.takewhile(lambda node: node != 'ZZZ', path))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
