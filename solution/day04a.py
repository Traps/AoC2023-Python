
import util

DAY_NUM: int = 4


def get_win_count(line:str) -> int:
    _,_,*numbers = line.split()
    div_pos = numbers.index('|')

    winning = set(numbers[:div_pos]).intersection(numbers[div_pos+1:])

    return len(winning)


def score_card(line:str) -> int:
    if win_count := get_win_count(line):
        return 2**(win_count - 1)

    return 0


def solve(_input: str) -> int:
    return sum(score_card(line) for line in _input.splitlines())


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
