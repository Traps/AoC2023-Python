import collections
import util

from solution.day04a import get_win_count


DAY_NUM: int = 4


def solve(_input: str) -> int:
    card_scores = [get_win_count(line) for line in _input.splitlines()]
    card_counts = collections.defaultdict(lambda: 1)

    for i_card, win_count in enumerate(card_scores):
        for j_win in range(i_card + 1, i_card + win_count + 1):
            card_counts[j_win] += card_counts[i_card]

    return sum(card_counts[i] for i in range(len(card_scores)))


if __name__ == '__main__':
    print(f'Day {DAY_NUM:02d}b answer: {solve(util.get_challenge(DAY_NUM))}')
