from typing import Final

import util

from solution.day14a import calculate_load


DAY_NUM: Final[int] = 14
TARGET_CYCLE_COUNT: Final[int] = 1000000000


def settle_rocks_north_west(content:str) -> str:
    if '.O' in content:
        return settle_rocks_north_west(content.replace('.O', 'O.'))

    return content


def settle_rocks_south_east(content:str) -> str:
    if 'O.' in content:
        return settle_rocks_south_east(content.replace('O.', '.O'))

    return content


def run_cycle(rows:tuple[str]) -> tuple[str]:
    columns = (settle_rocks_north_west(''.join(col)) for col in zip(*rows))
    rows = (settle_rocks_north_west(''.join(row)) for row in zip(*columns))
    columns = (settle_rocks_south_east(''.join(col)) for col in zip(*rows))
    rows = (settle_rocks_south_east(''.join(row)) for row in zip(*columns))

    return tuple(rows)


def solve(_input: str) -> int:
    lines = tuple(_input.splitlines())

    seen_states = {}
    for i_cycle in range(TARGET_CYCLE_COUNT):
        if lines in seen_states:
            break

        seen_states[lines] = i_cycle
        lines = run_cycle(lines)
    
    repeat_start = seen_states[lines]
    repeat_length = i_cycle - repeat_start
    
    end_cycle = (TARGET_CYCLE_COUNT - repeat_start) % repeat_length + repeat_start
    
    final_state = next(k for k,i in seen_states.items() if i==end_cycle)

    return sum(calculate_load(col) for col in zip(*final_state))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
    
