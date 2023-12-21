from aoc.utils import load_puzzle
from tqdm.auto import tqdm


def parse_puzzle(puzzle: str) -> list[str]:
    return [row.strip() for row in puzzle.strip().splitlines()]


def beam(grid: list[str], start: tuple[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
    # Beam starting from the top left corner going to the right
    num_rows = len(grid)
    num_cols = len(grid[0])
    beamed = []
    energized = []
    beams = [start]  # (tile, direction)
    while len(beams) > 0:
        # Beam
        beam, direction = beams.pop(0)
        beamed.append((beam, direction))
        next_tile = beam
        while True:
            # Ensure in bounds
            next_tile = (next_tile[0] + direction[0], next_tile[1] + direction[1])
            if next_tile[0] < 0 or next_tile[0] >= num_rows or next_tile[1] < 0 or next_tile[1] >= num_cols:
                break

            # Mark energized
            if next_tile not in energized:
                energized.append(next_tile)

            # Handle tiles
            next_tile_char = grid[next_tile[0]][next_tile[1]]
            if next_tile_char == "|" and abs(direction[1]) == 1:  # split vertically
                for new_beam in [(next_tile, (-1, 0)), (next_tile, (1, 0))]:
                    if new_beam not in beamed:
                        beams.append(new_beam)
                break
            elif next_tile_char == "-" and abs(direction[0]) == 1:  # split horizontally
                for new_beam in [(next_tile, (0, -1)), (next_tile, (0, 1))]:
                    if new_beam not in beamed:
                        beams.append(new_beam)
                break
            elif next_tile_char == "/":
                new_beam = (next_tile, (-direction[1], -direction[0]))
                if new_beam not in beamed:
                    beams.append(new_beam)
                break
            elif next_tile_char == "\\":
                new_beam = (next_tile, (direction[1], direction[0]))
                if new_beam not in beamed:
                    beams.append(new_beam)
                break

    return energized


def beam_all(grid: list[str]) -> list[tuple[int, int]]:
    # Generate all starting beams
    num_rows = len(grid)
    num_cols = len(grid[0])
    starts = []
    for row in range(num_rows):
        starts.append(((row, -1), (0, 1)))  # left -> right
        starts.append(((row, num_cols), (0, -1)))  # right -> left
    for col in range(num_cols):
        starts.append(((-1, col), (1, 0)))  # top -> bottom
        starts.append(((num_rows, col), (-1, 0)))  # bottom -> top

    # Beam
    max_energized: list[tuple[int, int]] = []
    for start in tqdm(starts):
        energized = beam(grid, start)
        if len(energized) > len(max_energized):
            max_energized = energized

    return max_energized


def solve_puzzle1(puzzle: str) -> int:
    grid = parse_puzzle(puzzle)
    energized = beam(grid, ((0, -1), (0, 1)))
    answer = len(energized)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    grid = parse_puzzle(puzzle)
    energized = beam_all(grid)
    answer = len(energized)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 7562
    assert solve_puzzle2(puzzle) == 7793
