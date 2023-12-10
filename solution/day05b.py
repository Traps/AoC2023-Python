import re
import z3
import util

DAY_NUM: int = 5


def parse_map(map_desc:str) -> tuple[str, str, tuple]:
    header, *rules = map_desc.splitlines()

    in_type, out_type = re.search(r'(\w+)-to-(\w+)', header).groups()

    map_rules = []
    for line in rules:
        dst, src, length = (int(v) for v in line.split())
        map_rules.append((src, src+length, dst-src))

    return in_type, out_type, map_rules


def make_rule(in_var:z3.Int, out_var:z3.Int, rule_ranges:list[tuple]):
    if len(rule_ranges) == 0:
        return (out_var == in_var)

    (in_min, in_max, offset), *rule_ranges = rule_ranges

    range_test = z3.And(in_var>=in_min, in_var<=in_max)
    range_output = (out_var == in_var + offset)

    return z3.If(range_test, range_output, make_rule(in_var, out_var, rule_ranges))


def solve(_input: str) -> int:
    seed_values, *maps = _input.split('\n\n')

    seed_values = tuple(int(s) for s in seed_values.split() if s.isnumeric())
    seed_ranges = tuple(zip(seed_values[0::2], seed_values[1::2]))

    resource = {'seed': z3.Int('seed')}

    opt = z3.Optimize()

    opt.add(z3.Or(*(z3.And(resource['seed'] >= r0, resource['seed'] <= r0+rw) for r0,rw in seed_ranges)))

    for mp in maps:
        in_type, out_type, ranges = parse_map(mp)

        in_var = resource[in_type]
        out_var = resource[out_type] = z3.Int(out_type)

        opt.add(make_rule(in_var, out_var, ranges))
    
    min_location = opt.minimize(resource['location'])
    
    if opt.check() == z3.sat:
        return min_location.value()
    

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
