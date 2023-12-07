import re

from aoc.utils import multiline_input

# Compile patterns
GAME_PTRN = re.compile(r"Game (\d+):")
CUBE_PTRN = re.compile(r"(\d+) (\w+)")

# Specify cubes in bag
BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _is_possible(line: str) -> tuple[int, bool]:
    game_id = int(GAME_PTRN.findall(line)[0])
    cube_sets = line.split(":")[-1].strip().split(";")
    for cube_set in cube_sets:
        for cubes in cube_set.split(", "):
            match = CUBE_PTRN.findall(cubes)[0]
            count = int(match[0])
            color = match[1]
            if count > BAG[color]:
                return game_id, False

    return game_id, True


def extract_numbers(puzzle: str) -> list[int]:
    numbers = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        game_id, is_possible = _is_possible(line)
        if is_possible:
            numbers.append(game_id)
    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
