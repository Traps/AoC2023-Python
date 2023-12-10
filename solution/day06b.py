import math

import util

DAY_NUM: int = 6


def charge_win_range(duration:int, record:int) -> range:
    c = math.sqrt(duration*duration - 4*record)

    charge_min = math.ceil((duration - c) / 2)
    charge_max = math.ceil((duration + c) / 2)

    return range(int(charge_min), int(charge_max))


def solve(_input: str) -> int:
    duration, record = (int(''.join(c for c in line if c.isnumeric()))
                            for line in _input.splitlines())
    
    win_range = charge_win_range(duration, record)

    return len(win_range)

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')

