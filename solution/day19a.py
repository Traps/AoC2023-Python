import collections
import dataclasses

from typing import Final

import util

DAY_NUM: Final[int] = 19


@dataclasses.dataclass(slots=True, frozen=True)
class Workflow(object):
    name:str
    rules:tuple

    def __call__(self, part:tuple[int,int,int,int]) -> bool:
        responses = (rule(part) for rule in self.rules)
        
        return next(res for res in responses if res is not None)
    
    @staticmethod
    def workflow_factory(definition:str, workflows:dict) -> dict:
        name, rules = definition[:-1].split('{')
        
        rules = tuple(Workflow.parse_rule(rule, workflows) for rule in rules.split(','))
        
        if any(rule is None for rule in rules):
            return None
        
        return Workflow(name, rules)
    
    @staticmethod
    def parse_rule(rule:str, workflows:dict) -> callable:
        if ':' not in rule:
            return workflows[rule] if rule in workflows else None
        
        condition, response = rule.split(':')

        if response not in workflows:
            return None

        rating = 'xmas'.index(condition[0])
        value = int(condition[2:])
        response = workflows[response]
        
        if condition[1] == '<':
            return lambda part: response(part) if part[rating] < value else None
         
        return lambda part: response(part) if part[rating] > value else None
    
    
def parse_part(part:str) -> tuple[int, int, int, int]:
    part = ''.join(c for c in part if c.isnumeric() or c==',')

    return tuple(int(rating) for rating in part.split(','))


def build_workflow(workflow_section:str) -> dict[str, Workflow]:
    workflows = {'A': lambda _: True, 'R': lambda _: False}
    
    workflow_definitions = collections.deque(workflow_section.splitlines())

    while workflow_definitions:
        workflow = Workflow.workflow_factory(workflow_definitions[-1], workflows)

        if workflow is None:
            workflow_definitions.rotate()
            continue
        
        workflows[workflow.name] = workflow
        workflow_definitions.pop()

    return workflows['in']
    

def solve(_input: str) -> int:
    workflow_definitions, part_lines = _input.split('\n\n')

    workflow_start = build_workflow(workflow_definitions)

    parts = (parse_part(line) for line in part_lines.splitlines())

    return sum(sum(part) for part in parts if workflow_start(part))
    

if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')