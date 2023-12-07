import re

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")


def extract_numbers(puzzle: str) -> list[int]:
    numbers = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        numbers_str = "".join(DIGIT_PTRN.findall(line))
        number = int(numbers_str[0] + numbers_str[-1])
        numbers.append(number)
    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
