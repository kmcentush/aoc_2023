import re

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")


def parse_puzzle(puzzle: str) -> tuple[int, int]:
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        line_strip = line.strip()
        if line_strip.startswith("Time: "):
            time = int("".join(DIGIT_PTRN.findall(line_strip)))
        elif line_strip.startswith("Distance: "):
            distance = int("".join(DIGIT_PTRN.findall(line_strip)))
    return time, distance


def extract_number(time: int, distance: int) -> int:
    number = 0
    for hold_time in range(1, time):
        speed = hold_time
        remaining_time = time - hold_time
        if remaining_time * speed > distance:
            number += 1
    return number


def solve_puzzle(puzzle: str) -> int:
    time, distance = parse_puzzle(puzzle)
    answer = extract_number(time, distance)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
