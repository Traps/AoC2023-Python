import util
import re

from solution.day01a import evaluate_line


DAY_NUM: int = 1


def digitize_input(_input:str) -> str:
    digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    
    number_indices = dict()
    for value, pattern in enumerate(digits, 1):
        number_indices[str(value)] = {m.span()[0] for m in re.finditer(pattern, _input)}
    
    _input = list(_input)
    for value, index in number_indices.items():
        for pos in index:
            _input[pos] = value
            
    return ''.join(_input)


def solve(_input: str) -> int:
    return sum(evaluate_line(line) for line in digitize_input(_input).splitlines())


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')