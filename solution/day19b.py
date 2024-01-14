import collections
import operator
import dataclasses
import math

from typing import Callable, Final

import util


DAY_NUM: Final[int] = 19


@dataclasses.dataclass(init=True, slots=True, frozen=True)
class ComparableRange(object):
    start:int
    stop:int

    def __lt__(self, value:int) -> tuple['ComparableRange', 'ComparableRange']:
        if value >= self.stop:
            return self, None
        
        if value < self.start:
            return None, self
        
        return ComparableRange(self.start, value), ComparableRange(value, self.stop)
    
    def __gt__(self, value:int) -> tuple['ComparableRange', 'ComparableRange']:
        if value < self.start:
            return self, None
        
        if value >= self.stop:
            return None, self

        return ComparableRange(value+1, self.stop), ComparableRange(self.start, value+1)
    
    def __len__(self) -> int:
        return self.stop - self.start


@dataclasses.dataclass(init=True, slots=True, frozen=True)
class Rule(object):
    rating:int
    operator:Callable
    value:int
    response:Callable
    fallback:'Rule'
    
    def __call__(self, part:dict) -> tuple[int, dict]:
        valid, invalid = self.operator(part[self.rating], self.value)

        return (0 if valid is None else self.response(part | {self.rating: valid})) \
                + (0 if invalid is None else self.fallback(part | {self.rating: invalid}))
    
    
    def factory(rules:list[str], workflows:dict) -> 'Rule':
        rule, *fallbacks = rules

        if ':' not in rule:
            return workflows[rule] if rule in workflows else None
        
        fallback = Rule.factory(fallbacks, workflows)
        if fallback is None:
            return None
        
        condition, response = rule.split(':')
        if response not in workflows:
            return None

        rating = 'xmas'.index(condition[0])
        op = operator.lt if condition[1] == '<' else operator.gt
        value = int(condition[2:])
        response = workflows[response]

        return Rule(rating, op, value, response, fallback)


def part_range_combinations(part:dict) -> int:
    return math.prod(len(v) for v in part.values())


def build_workflow(workflow_section:str) -> Rule:
    workflows = {'A': part_range_combinations, 'R': lambda _: 0}
    
    workflow_definitions = collections.deque(workflow_section.splitlines())

    while workflow_definitions:
        name, rules = workflow_definitions[-1].strip('}').split('{')
        
        workflow = Rule.factory(rules.split(','), workflows)

        if workflow is None:
            workflow_definitions.rotate()
            continue
        
        workflows[name] = workflow
        workflow_definitions.pop()

    return workflows['in']


def solve(_input: str) -> int:
    workflow_section, _ = _input.split('\n\n')

    workflow_start = build_workflow(workflow_section)

    variables = {0:ComparableRange(1,4001), 1:ComparableRange(1,4001),
                 2:ComparableRange(1,4001), 3:ComparableRange(1,4001)}
    
    return workflow_start(variables)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')