import collections

import util

from solution.day15a import calc_hash


DAY_NUM: int = 15

Step = collections.namedtuple('Step', ['lens_label', 'box_number', 'focal_length'])


def parse_step(step:str) -> Step:
    lens_label, focal_length = step.replace('-','=').split('=')

    box_number = calc_hash(lens_label)

    focal_length = int(focal_length) if focal_length else None

    return Step(lens_label, box_number, focal_length)


def run_step(step:Step, boxes:dict) -> None:
    box = boxes[step.box_number]

    if step.focal_length is not None:
        box[step.lens_label] = step.focal_length

    elif step.lens_label in box:
        box.pop(step.lens_label)
    
    return


def get_box_power(box:dict) -> int:
    return sum(i*fl for i,fl in enumerate(box.values(), 1))


def solve(_input: str) -> int:
    steps = (parse_step(step) for step in _input.split(','))
    
    boxes = collections.defaultdict(dict)

    for step in steps:
        run_step(step, boxes)

    return sum((i + 1)*get_box_power(box) for i,box in boxes.items())


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
