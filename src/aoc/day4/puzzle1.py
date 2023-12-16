import re

from aoc.utils import load_puzzle

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")


def _parse_card(line: str) -> tuple[list[int], list[int]]:
    line = line.split(":")[-1].strip()
    split = line.split("|")
    winning_numbers = [int(n) for n in DIGIT_PTRN.findall(split[0])]
    card_numbers = [int(n) for n in DIGIT_PTRN.findall(split[1])]
    return winning_numbers, card_numbers


def extract_numbers(puzzle: str) -> list[int]:
    numbers = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        winning_numbers, card_numbers = _parse_card(line)
        num_matches = 0
        for card_number in card_numbers:
            if card_number in winning_numbers:
                num_matches += 1
        if num_matches > 0:
            numbers.append(2 ** (num_matches - 1))
    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 27845
