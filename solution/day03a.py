import re
import util

DAY_NUM: int = 3

def has_adjacent_symbol(line_num:int, col0:int, col1:int, schematic:dict[int,str]) -> bool:
    is_symbol = lambda c: c not in '0123456789.'

    col_slice = slice(max(col0 - 1, 0), col1 + 1)

    for i_line in range(line_num-1, line_num+2):
        adjacent = schematic.get(i_line, '')[col_slice]

        if any(is_symbol(c) for c in adjacent):
            return True

    return False


def solve(_input: str) -> int:
    schematic = {i:line for i,line in enumerate(_input.splitlines())}
    
    part_sum = 0

    for line_num, line in schematic.items():
        for number in re.finditer(r'\d+', line):
            if has_adjacent_symbol(line_num, *number.span(), schematic):
                part_sum += int(number[0])

    return part_sum


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
