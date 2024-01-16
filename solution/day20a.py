import collections
import queue

from dataclasses import dataclass, field
from typing import Any, Callable, Final

import util

DAY_NUM: Final[int] = 20

@dataclass(slots=True, init=True, frozen=True)
class Pulse(object):
    level:bool
    source:'Module'
    destination:'Module'

    def __repr__(self) -> str:
        return f'Pulse(level={self.level}, source={self.source.name}, destination={self.destination.name})'
    

@dataclass(slots=True, unsafe_hash=True, eq=True)
class Module(object):
    name:str = field(hash=True, compare=True)
    downstream_modules:tuple['Module'] = field(hash=False, compare=False)

    def resolve_downstream_modules(self, modules:'defaultmoduledict') -> None:
        self.downstream_modules = tuple(modules[name] for name in self.downstream_modules)

        for module in self.downstream_modules:
            if isinstance(module, Conjunction):
                module.upstream_memory[self] = False

    def receive(self, pulse:Pulse, pulse_queue:queue.Queue) -> None:
        self.transmit(pulse.level, pulse_queue)

    def transmit(self, level:bool, pulse_queue:queue.Queue) -> None:
        for module in self.downstream_modules:
            pulse_queue.put_nowait(Pulse(level, self, module))


@dataclass(slots=True, unsafe_hash=True)
class FlipFlop(Module):
    state:bool = field(default=False, init=False, hash=False)

    def receive(self, pulse:Pulse, pulse_queue:queue.Queue) -> None:
        if not pulse.level:
            self.state = not self.state
        
            self.transmit(self.state, pulse_queue)


@dataclass(slots=True, unsafe_hash=True)
class Conjunction(Module):
    upstream_memory:dict[Module,bool] = field(default_factory=dict, init=False, hash=False)

    def receive(self, pulse:Pulse, pulse_queue:queue.Queue) -> None:
        self.upstream_memory[pulse.source] = pulse.level
        
        self.transmit(not all(self.upstream_memory.values()), pulse_queue)


def parse_module(module_definition:str) -> 'Module':
    name, downsteam = module_definition.split(' -> ')

    if name[0] == '%':
        return FlipFlop(name[1:], downsteam.split(', '))
    
    if name[0] == '&':
        return Conjunction(name[1:], downsteam.split(', '))
    
    return Module(name, downsteam.split(', '))


class defaultmoduledict(collections.defaultdict):
    default_factory: Callable[[], Any] = lambda: None

    def __missing__(self, __key: Any) -> Any:
        self[__key] = Module(__key, ())
        return self[__key]
    

def compile_modules(module_definitions:str) -> defaultmoduledict[str, Module]:
    modules = [parse_module(line) for line in module_definitions]
    
    modules = defaultmoduledict() | {module.name:module for module in modules}

    for module in list(modules.values()):
        module.resolve_downstream_modules(modules)

    return modules


def push_button(modules:dict) -> tuple[int, int]:
    pulse_queue = queue.SimpleQueue()
    pulse_queue.put_nowait(Pulse(False, modules['button'], modules['broadcaster']))
    
    while not pulse_queue.empty():
        pulse = pulse_queue.get_nowait()
        pulse.destination.receive(pulse, pulse_queue)
        
        yield pulse.level


def solve(_input: str) -> int:
    modules = compile_modules(_input.splitlines())

    pulse_count = {True: 0, False: 0}
    
    for _ in range(1000):
        for pulse in push_button(modules):
            pulse_count[pulse] += 1
    
    return pulse_count[True] * pulse_count[False]


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')