from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str, empty_scale: int) -> list[tuple[int, int]]:
    # Find empty rows and columns
    puzzle = puzzle.strip()
    valid_rows = []
    valid_cols = []
    for row, line in enumerate(puzzle.splitlines()):
        line_strip = line.strip()
        galaxy_cols = [pos for pos, char in enumerate(line_strip) if char == "#"]
        if len(galaxy_cols) > 0:
            valid_rows.append(row)
            valid_cols += galaxy_cols
    grid_size = (row, len(line_strip))
    empty_rows = set(range(grid_size[0])) - set(valid_rows)
    empty_cols = set(range(grid_size[1])) - set(valid_cols)

    # Find galaxies
    galaxies = []
    extra_rows = 0
    for row, line in enumerate(puzzle.splitlines()):
        # Skip empty rows
        if row in empty_rows:
            extra_rows += empty_scale - 1
            continue

        # Detect galaxies
        extra_cols = 0
        line_strip = line.strip()
        for col, char in enumerate(line_strip):
            # Skip empty columns
            if col in empty_cols:
                extra_cols += empty_scale - 1

            # Detect galaxies
            if char == "#":
                galaxies.append((row + extra_rows, col + extra_cols))

    return galaxies


def _find_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])  # Manhattan distance


def find_distances(galaxies: list[tuple[int, int]]) -> dict[tuple[tuple[int, int], tuple[int, int]], int]:
    distances = {}
    num_galaxies = len(galaxies)
    for i in range(num_galaxies):
        galaxy1 = galaxies[i]
        for j in range(i + 1, num_galaxies):
            galaxy2 = galaxies[j]
            distances[(galaxy1, galaxy2)] = _find_distance(galaxy1, galaxy2)
    return distances


def _solve_puzzle(puzzle: str, empty_scale: int) -> int:
    galaxies = parse_puzzle(puzzle, empty_scale=empty_scale)
    distances = find_distances(galaxies)
    answer = sum(distances.values())
    print(f"Answer: {answer}")
    return answer


def solve_puzzle1(puzzle: str) -> int:
    return _solve_puzzle(puzzle, empty_scale=2)


def solve_puzzle2(puzzle: str) -> int:
    return _solve_puzzle(puzzle, empty_scale=1000000)


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 9723824
    assert solve_puzzle2(puzzle) == 731244261352
