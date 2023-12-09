import re
from typing import Final

import util

DAY_NUM: Final[int] = 1
 
def evaluate_line(line:str, pattern:re.Pattern) -> int:
    matches = tuple(pattern.finditer(line))

    v0 = matches[0].groups().index('') + 1
    v1 = matches[-1].groups().index('') + 1

    return v0 * 10 + v1

def parse_input(_input:str) -> list[int]:
    numbers = ('one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine')
    
    groups = [f'((?={i}|{num}))' for i,num in enumerate(numbers, 1)]
    groups.insert(0, r'((?=\n))')

    pattern = re.compile(fr'(?:{"|".join(groups)})')

    matches = pattern.finditer(_input)
    match_groups = [m.groups().index('') for m in  matches]


def solve(_input: str) -> int:
    numbers = ('one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine')
    
    groups = (f'((?={i}|{num}))' for i,num in enumerate(numbers, 1))

    pattern = re.compile(fr'(?:{"|".join(groups)})')

    return sum(evaluate_line(line, pattern) for line in _input.splitlines())


if __name__ == '__main__':
    parse_input(util.get_sample(1,'b'))
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')