import re
from functools import reduce

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")


def parse_puzzle(puzzle: str) -> tuple[list[int], list[int]]:
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        line_strip = line.strip()
        if line_strip.startswith("Time: "):
            times = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
        elif line_strip.startswith("Distance: "):
            distances = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
    return times, distances


def extract_numbers(times: list[int], distances: list[int]) -> list[int]:
    numbers = []
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        number = 0
        for hold_time in range(1, time):
            speed = hold_time
            remaining_time = time - hold_time
            if remaining_time * speed > distance:
                number += 1
        numbers.append(number)
    return numbers


def _product(vals: list[int]) -> int:
    return reduce(lambda x, y: x * y, vals)


def solve_puzzle(puzzle: str) -> int:
    times, distances = parse_puzzle(puzzle)
    numbers = extract_numbers(times, distances)
    answer = _product(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
