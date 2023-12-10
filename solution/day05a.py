import dataclasses
import re
import util

DAY_NUM: int = 5

@dataclasses.dataclass(slots=True)
class RangeMap(object):
    in_type : str
    out_type : str

    ranges : tuple[range, int]

    def apply(self, value:int):
        offset = next((offs for rng,offs in self.ranges if value in rng), 0)

        return value + offset
    
    @staticmethod
    def parse_map(map_description:str) -> 'RangeMap':
        name, *range_lines = map_description.splitlines()

        in_type, out_type = re.search(r'(\w+)-to-(\w+)', name).groups()

        ranges = []
        for line in range_lines:
            dst, src, length = (int(v) for v in line.split())
            ranges.append((range(src, src+length+1), dst - src))

        return RangeMap(in_type=in_type, out_type=out_type, ranges=tuple(ranges))


def solve(_input: str) -> int:
    seeds, *maps = _input.split('\n\n')

    values = tuple(int(s) for s in seeds.split() if s.isnumeric())

    maps = tuple(RangeMap.parse_map(m) for m in maps)

    for mp in maps:
        values = tuple(mp.apply(v) for v in values)
    
    return min(values)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
