from collections import defaultdict

from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str) -> tuple[list[str], list[str]]:
    rows: list[str] = []
    cols_dict: dict[int, str] = defaultdict(lambda: "")
    for row in puzzle.strip().splitlines():
        row_strip = row.strip()
        rows.append(row_strip)
        for i in range(len(row_strip)):
            cols_dict[i] += row_strip[i]
    cols = list(cols_dict.values())

    return rows, cols


def _roll(vals: str) -> str:
    # Get rock locations
    round_rocks = []
    cube_rocks = []
    for i, char in enumerate(vals):
        if char == "O":
            round_rocks.append(i)
        elif char == "#":
            cube_rocks.append(i)
    cube_rocks.append(i + 1)  # spoof a cube rock at the outer edge

    # Roll
    new_round_rocks = []
    did_roll = []
    min_idx = -1
    for cube_rock in cube_rocks:
        can_roll = [r for r in round_rocks if r < cube_rock and r not in did_roll]
        new_round_rocks += [min_idx + 1 + i for i in range(len(can_roll))]
        min_idx = cube_rock
        did_roll += can_roll

    # Convert to string
    out = ""
    for i in range(len(vals)):
        if i in new_round_rocks:
            out += "O"
        elif i in cube_rocks:
            out += "#"
        else:
            out += "."

    return out


def _rotate(cols: list[str]):
    rows_dict: dict[int, str] = defaultdict(lambda: "")
    for col in cols:
        for i, char in enumerate(col):
            rows_dict[i] += char
    return list(rows_dict.values())


def roll(direction: str, rows: list[str], cols: list[str]) -> tuple[list[str], list[str]]:
    if direction == "N":
        rolled_cols = [_roll(col) for col in cols]
        rolled_rows = _rotate(rolled_cols)
    elif direction == "S":
        flipped_cols = [col[::-1] for col in cols]  # reverse string
        flipped_rolled_cols = [_roll(col) for col in flipped_cols]
        rolled_cols = [col[::-1] for col in flipped_rolled_cols]  # reverse back
        rolled_rows = _rotate(rolled_cols)
    elif direction == "W":
        rolled_rows = [_roll(row) for row in rows]
        rolled_cols = _rotate(rolled_rows)
    elif direction == "E":
        flipped_rows = [row[::-1] for row in rows]  # reverse string
        flipped_rolled_rows = [_roll(row) for row in flipped_rows]
        rolled_rows = [row[::-1] for row in flipped_rolled_rows]  # reverse back
        rolled_cols = _rotate(rolled_rows)

    return rolled_rows, rolled_cols


def calculate_load(rows: list[str]) -> int:
    rows_len = len(rows)
    load = 0
    for i, row in enumerate(rows):
        round_rocks = row.count("O")
        load += round_rocks * (rows_len - i)
    return load


def solve_puzzle1(puzzle: str) -> int:
    rows, cols = parse_puzzle(puzzle)
    rows, cols = roll("N", rows, cols)
    answer = calculate_load(rows)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    rows, cols = parse_puzzle(puzzle)
    directions = "NWSE"
    directions_len = len(directions)
    for i in range(1000000000):
        direction = directions[i % directions_len]
        rows, cols = roll(direction, rows, cols)
    answer = calculate_load(rows)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 103333
    # assert solve_puzzle2(puzzle) ==
