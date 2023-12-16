import re

from aoc.utils import load_puzzle

# Compile patterns
CUBE_PTRN = re.compile(r"(\d+) (\w+)")


def _extract_min_counts(line: str) -> tuple[int, int, int]:
    min_bag = {"red": 0, "green": 0, "blue": 0}
    cube_sets = line.split(":")[-1].strip().split(";")
    for cube_set in cube_sets:
        for cubes in cube_set.split(", "):
            match = CUBE_PTRN.findall(cubes)[0]
            count = int(match[0])
            color = match[1]
            if count > min_bag[color]:
                min_bag[color] = count

    return min_bag["red"], min_bag["green"], min_bag["blue"]


def extract_numbers(puzzle: str) -> list[int]:
    numbers = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        red_count, green_count, blue_count = _extract_min_counts(line)
        power = red_count * green_count * blue_count
        numbers.append(power)
    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 56580
