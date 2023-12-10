import util

DAY_NUM: int = 7

CARD_INDICES : str = '23456789TJQKA'

def parse_hand(hand:str) -> str:
    for value, card in enumerate(CARD_INDICES, ord('a')):
        hand = hand.replace(card, chr(value))

    unique_count = len(set(hand))
    most_common_count = max(hand.count(c) for c in hand)
    
    match unique_count, most_common_count:
        case 1, _: # Five of a kind
            return f'6{hand}'
        case 2, 4: # Four of a kind
            return f'5{hand}'
        case 2, _: # Full house
            return f'4{hand}'
        case 3, 3: # Three of a kind
            return f'3{hand}'
        case 3, _: # Two pairs
            return f'2{hand}'
        case 4, _: # One pair
            return f'1{hand}'
        case _: # High card
            return f'0{hand}'


def solve(_input: str) -> int:
    players = (line.split() for line in _input.splitlines())
    players = [(parse_hand(hand), int(bet)) for hand, bet in players]

    return sum(rank*bet for rank,(_,bet) in enumerate(sorted(players), 1))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}a answer: {solve(util.get_challenge(DAY_NUM))}')
