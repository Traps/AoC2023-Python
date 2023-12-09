import util

from solution.day02a import parse_game

DAY_NUM: int = 2


def get_game_power(rounds:list) -> int:
    return (max(r.get('red', 1) for r in rounds) *
            max(r.get('green', 1) for r in rounds) *
            max(r.get('blue', 1) for r in rounds) )
    

def solve(_input: str) -> int:
    games = (parse_game(line) for line in _input.splitlines())
    
    return sum(get_game_power(rounds) for _,rounds in games)


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
