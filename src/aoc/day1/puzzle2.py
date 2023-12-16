import re

from aoc.utils import load_puzzle

# Specify digits
DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGITS = list(DIGIT_MAP.keys()) + list("123456789")
DIGITS_PTRNS = [re.compile(v) for v in DIGITS]


def _str_to_digits(line: str) -> str:
    # Find indices of matches
    matches = {}
    for ptrn in DIGITS_PTRNS:
        for match in ptrn.finditer(line):
            matches[match.start()] = match.group()

    # Reconstruct input
    out = ""
    matches = dict(sorted(matches.items()))
    for val in matches.values():
        if val in DIGIT_MAP.keys():
            out += DIGIT_MAP[val]
        else:
            out += val

    return out


def extract_numbers(puzzle: str) -> list[int]:
    numbers = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        numbers_str = _str_to_digits(line)
        number = int(numbers_str[0] + numbers_str[-1])
        numbers.append(number)
    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 53894
