import util

DAY_NUM: int = 7

CARD_INDICES : str = 'J23456789TQKA'

def evaluate_hand(hand:str) -> str:
    joker_count = hand.count('J')
    unique_count = len(set(hand))
    most_common_count = max(hand.count(c) for c in hand)

    for value, card in enumerate(CARD_INDICES, ord('a')):
        hand = hand.replace(card, chr(value))

    match (unique_count, joker_count, most_common_count):
        case 1, _, _: # Five of a kind
            return f'6{hand}' 
        case 2, 0, 4: # Four of a kind
            return f'5{hand}' 
        case 2, 0, _: # Full house
            return f'4{hand}'
        case 2, _, _: # Four of a kind / Full house + joker
            return f'6{hand}'
        case 3, 0, 3: # Three of a kind
            return f'3{hand}'
        case 3, _, 3: # Three of a kind + joker
            return f'5{hand}'
        case 3, 2, _: # Two pairs + two jokers 
            return f'5{hand}' # Four of a kind
        case 3, 1, _: # Two pairs + one joker
            return f'4{hand}' # Full house
        case 3, 0, _: # Two pairs
            return f'2{hand}'
        case 4, 0, _: # One pair, no jokers
            return f'1{hand}'
        case 4, _, _: # One pair and at least one joker
            return f'3{hand}'
        case _, 1, _: # High card and a joker
            return f'1{hand}'
        case _: # High card
            return f'0{hand}'


def solve(_input: str) -> int:
    players = (line.split() for line in _input.splitlines())
    players = [(evaluate_hand(hand), int(bet)) for hand, bet in players]

    return sum(rank*bet for rank,(_,bet) in enumerate(sorted(players), 1))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
