import collections
import re
import util

DAY_NUM: int = 3

def find_gear(line_num:int, col0:int, col1:int, schematic:dict[int,str]) -> bool:
    col_slice = slice(max(col0 - 1, 0), col1 + 1)

    for i_line in range(line_num-1, line_num+2):
        adjacent = schematic.get(i_line, '')[col_slice]

        if '*' in adjacent:
            return (i_line, col_slice.start + adjacent.index('*'))


def solve(_input: str) -> int:
    schematic = {i:line for i,line in enumerate(_input.splitlines())}
    
    gears = collections.defaultdict(list)

    for line_num, line in schematic.items():
        for number in re.finditer(r'\d+', line):
            gear_location = find_gear(line_num, *number.span(), schematic)

            if gear_location is not None:
                gears[gear_location].append(int(number[0]))


    for loc,values in gears.items():
        print(loc, values)

    return sum(g[0] * g[1] for g in gears.values() if len(g)==2)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
