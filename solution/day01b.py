import itertools
import re
from typing import Final, Iterator

import util

DAY_NUM: Final[int] = 1

def parse_lines(_input:str) -> Iterator[int]:
    numbers = ('one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine')
    
    groups = (f'((?={i}|{num}))' for i,num in enumerate(numbers, 1))

    matches = re.finditer(fr'(?:((?=\n))|{"|".join(groups)})', _input)

    values = (m.groups().index('') for m in matches)

    while line_values := tuple(itertools.takewhile(lambda i: i!= 0, values)):
        yield line_values[0] * 10 + line_values[-1]
        

def solve(_input: str) -> int:
    return sum(value for value in parse_lines(_input))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')