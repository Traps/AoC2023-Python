import collections
import re

import util

DAY_NUM: int = 10

def parse_pipes(_input:str) -> dict[tuple, list[tuple]]:
    h_connected = re.compile('[FL\-S](?=[7J\-S])')
    v_connected = re.compile('[F7\|S](?=[LJ\|S])') 

    lines = _input.splitlines()
    connections = collections.defaultdict(list)

    for j,line in enumerate(lines):
        for match in h_connected.finditer(line):
            node0 = (match.span()[0], j)
            node1 = (match.span()[1], j)

            connections[node0].append(node1)
            connections[node1].append(node0)

        if 'S' in line:
            start_pos = (line.index('S'), j)

    for i,column in enumerate(''.join(col) for col in zip(*lines)):
        for match in v_connected.finditer(column):
            node0 = (i, match.span()[0])
            node1 = (i, match.span()[1])

            connections[node0].append(node1)
            connections[node1].append(node0)
    
    return start_pos, dict(connections)


def evaluate_distances(start_pos:tuple, connections:dict) -> dict[tuple, int]:
    distances = {start_pos: 0}
    to_visit = {start_pos}

    max_length = len(connections)

    while to_visit:
        node = to_visit.pop()
        next_distance = distances[node] + 1

        for neighbour in connections.get(node, ()):
            if distances.get(neighbour, max_length) > next_distance:
                distances[neighbour] = next_distance
                to_visit.add(neighbour)

    return distances


def solve(_input: str) -> int:
    start_pos, connections = parse_pipes(_input)
    
    distances = evaluate_distances(start_pos, connections)

    return max(distances.values())
    

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
