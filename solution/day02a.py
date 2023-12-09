import re
import util

DAY_NUM: int = 2

def parse_round(_round:str) -> dict:
    return {col: int(cnt) for cnt,col in re.findall(r'(?:(\d+) (\w+))', _round)}

def parse_game(line:str) -> tuple[int, tuple]:
    pattern = r'Game (\d*): (.+)'

    game_id, rounds = re.match(pattern, line).groups()

    game_rounds = tuple(parse_round(r) for r in rounds.split(';'))
    
    return (int(game_id), game_rounds)

def validate_round(game_round: dict[str, int]) -> bool:
    limits = {'red': 12, 'green': 13, 'blue': 14}

    return all(game_round.get(color,0) <= limit for color,limit in limits.items())


def solve(_input: str) -> int:
    games = (parse_game(line) for line in _input.splitlines())

    return sum(i for i,rounds in games if all(validate_round(r) for r in rounds))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
