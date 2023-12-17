import re
from functools import cache

from aoc.utils import load_puzzle

# Compile patterns
DIGIT_PTRN = re.compile(r"(\d+)")


def parse_puzzle(puzzle: str) -> list[tuple[str, tuple[int, ...]]]:
    lines = []
    for line in puzzle.strip().splitlines():
        split = line.strip().split(" ")
        counts = [int(d) for d in DIGIT_PTRN.findall(split[1])]
        lines.append((split[0], tuple(counts)))
    return lines


@cache
def _find_arrangements(line: str, counts: tuple[int, ...]) -> int:
    # Handle no more groups
    counts_len = len(counts)
    if counts_len == 0:
        return "#" not in line

    # Ensure enough possible combinations
    # (I don't fully understand this...)
    line_len = len(line)
    if line_len - sum(counts) - len(counts) + 1 < 0:
        return 0

    # Check current group
    group_len = counts[0]
    group_len_chars = line[0:group_len]
    has_holes = any(c == "." for c in group_len_chars)
    if line_len == group_len:
        return not has_holes

    # Handle completed groups
    can_use = not has_holes and line[group_len] != "#"
    if can_use:  # group is completed; next character must be a period, so we can skip over it
        new_line = line[group_len + 1 : :].lstrip(".")
        used = _find_arrangements(new_line, counts[1::])
    else:
        used = 0

    # Handle "#"
    if line[0] == "#":
        return used if can_use else 0

    # Handle "?" and "."
    new_line = line[1::].lstrip(".")
    skip = _find_arrangements(new_line, counts)
    if not can_use:
        return skip
    else:
        return skip + used


def find_arrangements(lines: list[tuple[str, tuple[int, ...]]]) -> list[int]:
    arrangements = []
    for line, counts in lines:
        arrangements.append(_find_arrangements(line, counts))
    return arrangements


def _solve_puzzle(puzzle: str, copies: int) -> int:
    lines = parse_puzzle(puzzle)
    lines = [("?".join([v[0]] * copies), v[1] * copies) for v in lines]
    arrangements = find_arrangements(lines)
    answer = sum(arrangements)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle1(puzzle: str) -> int:
    return _solve_puzzle(puzzle, copies=1)


def solve_puzzle2(puzzle: str) -> int:
    return _solve_puzzle(puzzle, copies=5)


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 7379
    assert solve_puzzle2(puzzle) == 7732028747925
