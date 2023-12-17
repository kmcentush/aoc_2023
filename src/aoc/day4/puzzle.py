import re
from collections import defaultdict
from copy import deepcopy

from aoc.utils import load_puzzle

# Compile patterns
CARD_PTRN = re.compile(r"Card +(\d+):")
DIGIT_PTRN = re.compile(r"\d+")


def _parse_card(line: str) -> tuple[int, list[int], list[int]]:
    card_id = int(CARD_PTRN.findall(line)[0])
    line = line.split(":")[-1].strip()
    split = line.split("|")
    winning_numbers = [int(n) for n in DIGIT_PTRN.findall(split[0])]
    card_numbers = [int(n) for n in DIGIT_PTRN.findall(split[1])]
    return card_id, winning_numbers, card_numbers


def find_winners(puzzle: str) -> dict[int, int]:
    cards = {}
    for line in puzzle.strip().splitlines():
        card_id, winning_numbers, card_numbers = _parse_card(line)
        num_matches = 0
        for card_number in card_numbers:
            if card_number in winning_numbers:
                num_matches += 1
        cards[card_id] = num_matches

    return cards


def score_winners1(cards: dict[int, int]) -> list[int]:
    return [2 ** (num_matches - 1) for num_matches in cards.values() if num_matches > 0]


def score_winners2(cards: dict[int, int]) -> dict[int, int]:
    cards_list = {card_id: [card_id + i + 1 for i in range(num_matches)] for card_id, num_matches in cards.items()}
    orig_cards_list = deepcopy(cards_list)  # `cards_list` mutates in loops
    numbers: dict[int, int] = defaultdict(lambda: 0)
    for card_id in cards.keys():
        numbers[card_id] += 1
        new_card_ids = cards_list[card_id]
        for new_card_id in new_card_ids:
            numbers[new_card_id] += 1
            cards_list[new_card_id] += orig_cards_list[new_card_id]
    return numbers


def solve_puzzle1(puzzle: str) -> int:
    winners = find_winners(puzzle)
    numbers = score_winners1(winners)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    winners = find_winners(puzzle)
    numbers = score_winners2(winners)
    answer = sum(numbers.values())
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 27845
    assert solve_puzzle2(puzzle) == 9496801
