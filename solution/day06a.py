import util

DAY_NUM: int = 6


def get_distance(charge_ms:int, total_ms:int) -> int:
    return (total_ms - charge_ms) * charge_ms


def solve(_input: str) -> int:
    durations, records = ([int(v) for v in line.split() if v.isnumeric()]
                            for line in _input.splitlines())
    
    product = 1
    for duration, record in zip(durations, records):
        product *= sum(get_distance(c_ms, duration) > record
                        for c_ms in range(duration))
    
    return product


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
