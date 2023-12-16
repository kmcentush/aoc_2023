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


def extract_numbers(puzzle: str) -> dict[int, int]:
    # Prepare to extract
    puzzle = puzzle.strip()

    # Find how many cards each win
    cards = {}
    for line in puzzle.splitlines():
        card_id, winning_numbers, card_numbers = _parse_card(line)
        num_matches = 0
        for card_number in card_numbers:
            if card_number in winning_numbers:
                num_matches += 1
        cards[card_id] = [card_id + i + 1 for i in range(num_matches)]

    # Count winners
    orig_cards = deepcopy(cards)  # `cards` mutates in loops
    numbers: dict[int, int] = defaultdict(lambda: 0)
    for card_id in cards.keys():
        numbers[card_id] += 1
        for new_card_id in cards[card_id]:
            numbers[new_card_id] += 1
            cards[new_card_id] += orig_cards[new_card_id]

    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers.values())
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 9496801
