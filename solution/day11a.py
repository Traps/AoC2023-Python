import collections
import itertools
from typing import Iterable, Iterator

import util

DAY_NUM: int = 11

Galaxy = collections.namedtuple('Galaxy', ['x', 'y'])


def locate_galaxies(image:str, empty_padding:int=1) -> list[Galaxy]:
    rows = image.splitlines()

    padding_rows = itertools.accumulate('#' not in row for row in rows)
    padding_rows = tuple(n_pad * empty_padding for n_pad in padding_rows)

    padding_cols = itertools.accumulate('#' not in col for col in zip(*rows))
    padding_cols = tuple(n_pad * empty_padding for n_pad in padding_cols)
    
    return [Galaxy(i + padding_cols[i], j + padding_rows[j]) 
                for j,row in enumerate(rows)
                for i,pixel in enumerate(row) 
                if pixel=='#']

  
def pair_distances(galaxies:Iterable[Galaxy]) -> Iterator[int]:
    for galaxy0, galaxy1 in itertools.combinations(galaxies, 2):
        yield abs(galaxy0.x - galaxy1.x) + abs(galaxy0.y - galaxy1.y)


def solve(_input: str) -> int:
    galaxies = locate_galaxies(_input)

    return sum(pair_distances(galaxies))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
