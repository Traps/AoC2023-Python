import util

from solution.day11a import locate_galaxies, pair_distances

DAY_NUM: int = 11


def solve(_input: str, expansion_multiplier:int=1000000) -> int:
    galaxies = locate_galaxies(_input, expansion_multiplier - 1)

    return sum(pair_distances(galaxies))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
