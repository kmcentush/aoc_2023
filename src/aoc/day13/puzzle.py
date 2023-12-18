from collections import defaultdict

from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str) -> list[tuple[list[str], list[str]]]:
    games = []
    rows: list[str] = []
    cols_dict: dict[int, str] = defaultdict(lambda: "")
    for row in puzzle.strip().splitlines():
        row_strip = row.strip()

        # Split games
        if len(row_strip) == 0:
            # Append
            cols = list(cols_dict.values())
            games.append((rows, cols))

            # Reset
            rows = []
            cols_dict = defaultdict(lambda: "")
            continue

        # Build values
        rows.append(row_strip)
        for i in range(len(row_strip)):
            cols_dict[i] += row_strip[i]

    # Append last game
    cols = list(cols_dict.values())
    games.append((rows, cols))

    return games


def _find_mirror(vals: list[str]) -> int:
    # Find entries to check
    num_vals = len(vals)
    to_check = []
    for i in range(num_vals - 1):
        to_check.append((i, i + 1))

    # Check entries
    for first_idx, second_idx in to_check:
        # Ensure we start from symmetry
        if vals[first_idx] != vals[second_idx]:
            continue

        # Explore outward
        before_idx = first_idx - 1
        after_idx = second_idx + 1
        is_mirror = True
        while before_idx >= 0 and after_idx < num_vals:
            if vals[before_idx] != vals[after_idx]:
                is_mirror = False
                break
            before_idx -= 1
            after_idx += 1
        if is_mirror:
            return second_idx  # number of entries before symmetry

    return 0


def find_mirrors(games: list[tuple[list[str], list[str]]]) -> tuple[list[int], list[int]]:
    row_mirrors = []
    col_mirrors = []
    for rows, cols in games:
        row_mirrors.append(_find_mirror(rows))
        col_mirrors.append(_find_mirror(cols))
    return row_mirrors, col_mirrors


def solve_puzzle1(puzzle: str) -> int:
    games = parse_puzzle(puzzle)
    row_mirrors, col_mirrors = find_mirrors(games)
    answer = sum(row_mirrors) * 100 + sum(col_mirrors)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 33047
    # assert solve_puzzle2(puzzle) == ?
