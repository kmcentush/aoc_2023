from typing import TYPE_CHECKING

from aoc.utils import load_puzzle

if TYPE_CHECKING:
    from collections.abc import Sequence


def parse_puzzle(puzzle: str) -> tuple[list[str], tuple[int, int]]:
    grid = []
    for i, row in enumerate(puzzle.strip().splitlines()):
        row_strip = row.strip()
        grid.append(row_strip)
        if "S" in row_strip:
            start = (i, row_strip.index("S"))

    return grid, start


def step(
    grid: list[str], start: tuple[int, int], max_steps: int, allow_infinite: bool = False
) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    # Prepare to take steps
    num_rows = len(grid)
    num_cols = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Take steps
    queue = [(max_steps, start, (0, 0))]
    plots: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    seen = set()
    while queue:
        # Get setup
        steps_remaining, node, repeat = queue.pop(0)

        # Ensure we can step
        if steps_remaining < 0:
            continue

        # We can always get back to a location in an even number of steps
        if steps_remaining % 2 == 0:
            plots.add((node, repeat))

        # Take a step
        steps_remaining -= 1
        for direction in directions:
            # Handle repeat grids
            new_node = node[0] + direction[0], node[1] + direction[1]
            new_repeat = repeat
            if new_node[0] < 0:
                if not allow_infinite:
                    continue
                new_repeat = (new_repeat[0] - 1, new_repeat[1])
                new_node = (new_node[0] + num_rows, new_node[1])
            elif new_node[0] >= num_rows:
                if not allow_infinite:
                    continue
                new_repeat = (new_repeat[0] + 1, new_repeat[1])
                new_node = (new_node[0] - num_rows, new_node[1])
            if new_node[1] < 0:
                if not allow_infinite:
                    continue
                new_repeat = (new_repeat[0], new_repeat[1] - 1)
                new_node = (new_node[0], new_node[1] + num_cols)
            elif new_node[1] >= num_cols:
                if not allow_infinite:
                    continue
                new_repeat = (new_repeat[0], new_repeat[1] + 1)
                new_node = (new_node[0], new_node[1] - num_cols)

            # Handle seen and rocks
            maybe_seen = (new_node, new_repeat)
            if maybe_seen in seen or grid[new_node[0]][new_node[1]] == "#":
                continue

            # Append
            queue.append((steps_remaining, new_node, new_repeat))
            seen.add(maybe_seen)

    return plots


def quad(y: "Sequence[float]", x: float) -> float:
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * x**2) + (b * x) + c


def solve_puzzle1(puzzle: str, max_steps: int) -> int:
    grid, start = parse_puzzle(puzzle)
    plots = step(grid, start, max_steps, allow_infinite=False)
    answer = len(plots)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str, max_steps: int) -> int:
    """T
    his is incredibly tricky. I would never have figured this out.

    https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    """
    # Get grid
    grid, start = parse_puzzle(puzzle)
    assert len(grid) == len(grid[0])  # square

    # Get first three plot counts
    size = len(grid)
    edge = size // 2
    steps = [edge + i * size for i in range(3)]  # need three points to fit a quadratic
    num_plots = [len(step(grid, start, s, allow_infinite=True)) for s in steps]

    # Fit and use quadratic
    answer = int(quad(num_plots, ((max_steps - edge) // size)))
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle, 64) == 3642
    assert solve_puzzle2(puzzle, 26501365) == 608603023105276
