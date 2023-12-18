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


def _maybe_smudge(line1: str, line2: str) -> bool:
    diff = [line1[i] != line2[i] for i in range(len(line1))]
    return sum(diff) == 1


def _find_mirror(vals: list[str], orig_idx: int) -> int:
    # Find entries to check
    num_vals = len(vals)
    to_check = []
    for i in range(num_vals - 1):
        to_check.append((i, i + 1))

    # Check entries
    allow_smudge = orig_idx != -1
    for first_idx, second_idx in to_check:
        # Allow one smudge
        did_smudge = False

        # Ensure we start from symmetry
        if vals[first_idx] != vals[second_idx]:
            if allow_smudge and not did_smudge and _maybe_smudge(vals[first_idx], vals[second_idx]):
                did_smudge = True
            else:
                continue

        # Explore outward
        before_idx = first_idx - 1
        after_idx = second_idx + 1
        is_mirror = True
        while before_idx >= 0 and after_idx < num_vals:
            if vals[before_idx] != vals[after_idx]:
                if allow_smudge and not did_smudge and _maybe_smudge(vals[before_idx], vals[after_idx]):
                    did_smudge = True
                else:
                    is_mirror = False
                    break
            before_idx -= 1
            after_idx += 1
        if is_mirror and second_idx != orig_idx:
            return second_idx  # number of entries before symmetry

    return 0


def find_mirrors(
    games: list[tuple[list[str], list[str]]],
    allow_smudge: bool,
    orig_row_mirrors: list[int] = [],
    orig_col_mirrors: list[int] = [],
) -> tuple[list[int], list[int]]:
    row_mirrors = []
    col_mirrors = []
    for i, (rows, cols) in enumerate(games):
        orig_row_idx = orig_row_mirrors[i] if allow_smudge else -1
        row_mirrors.append(_find_mirror(rows, orig_row_idx))
        orig_col_idx = orig_col_mirrors[i] if allow_smudge else -1
        col_mirrors.append(_find_mirror(cols, orig_col_idx))
    return row_mirrors, col_mirrors


def solve_puzzle1(puzzle: str) -> int:
    games = parse_puzzle(puzzle)
    row_mirrors, col_mirrors = find_mirrors(games, False)
    answer = sum(row_mirrors) * 100 + sum(col_mirrors)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    games = parse_puzzle(puzzle)
    row_mirrors, col_mirrors = find_mirrors(games, False)
    row_mirrors_smudge, col_mirrors_smudge = find_mirrors(games, True, row_mirrors, col_mirrors)
    answer = sum(row_mirrors_smudge) * 100 + sum(col_mirrors_smudge)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 33047
    assert solve_puzzle2(puzzle) == 28806
