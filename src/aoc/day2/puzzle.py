import re

from aoc.utils import load_puzzle

# Compile patterns
GAME_PTRN = re.compile(r"Game (\d+):")
CUBE_PTRN = re.compile(r"(\d+) (\w+)")


def _extract_min_counts(line: str) -> tuple[int, int, int, int]:
    min_bag = {"red": 0, "green": 0, "blue": 0}
    game_id = int(GAME_PTRN.findall(line)[0])
    cube_sets = line.split(":")[-1].strip().split(";")
    for cube_set in cube_sets:
        for cubes in cube_set.split(", "):
            match = CUBE_PTRN.findall(cubes)[0]
            count = int(match[0])
            color = match[1]
            if count > min_bag[color]:
                min_bag[color] = count

    return game_id, min_bag["red"], min_bag["green"], min_bag["blue"]


def extract_min_counts(puzzle: str) -> dict[int, tuple[int, int, int]]:
    counts = {}
    for line in puzzle.strip().splitlines():
        game_id, red_count, green_count, blue_count = _extract_min_counts(line)
        counts[game_id] = (red_count, green_count, blue_count)

    return counts


def score_games1(counts: dict[int, tuple[int, int, int]]) -> list[int]:
    numbers = []
    for game_id, (red_count, green_count, blue_count) in counts.items():
        if red_count <= 12 and green_count <= 13 and blue_count <= 14:  # ensure possible
            numbers.append(game_id)
    return numbers


def score_games2(counts: dict[int, tuple[int, int, int]]) -> list[int]:
    numbers = []
    for red_count, green_count, blue_count in counts.values():
        power = red_count * green_count * blue_count
        numbers.append(power)
    return numbers


def solve_puzzle1(puzzle: str) -> int:
    counts = extract_min_counts(puzzle)
    numbers = score_games1(counts)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    counts = extract_min_counts(puzzle)
    numbers = score_games2(counts)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 2727
    assert solve_puzzle2(puzzle) == 56580
