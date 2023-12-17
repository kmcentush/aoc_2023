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


def find_winners(puzzle: str) -> dict[int, list[int]]:
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

    return cards


def score_winners1(cards: dict[int, list[int]]) -> list[int]:
    numbers = []
    for card_id, new_card_ids in cards.items():
        if len(new_card_ids) > 0:
            num_matches = new_card_ids[-1] - card_id
            if num_matches > 0:
                numbers.append(2 ** (num_matches - 1))
    return numbers


def score_winners2(cards: dict[int, list[int]]) -> dict[int, int]:
    # Count winners
    orig_cards = deepcopy(cards)  # `cards` mutates in loops
    numbers: dict[int, int] = defaultdict(lambda: 0)
    for card_id in cards.keys():
        numbers[card_id] += 1
        for new_card_id in cards[card_id]:
            numbers[new_card_id] += 1
            cards[new_card_id] += orig_cards[new_card_id]

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
