import functools

import util

DAY_NUM: int = 15


def hash_func(accumulator:int, character:str) -> int:
    return (accumulator + ord(character)) * 17 % 256


def calc_hash(step:str) -> int:
    return functools.reduce(hash_func, step, 0)


def solve(_input: str) -> int:
    return sum(calc_hash(step) for step in _input.split(','))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
