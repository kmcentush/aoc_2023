from math import gcd

from aoc.utils import load_puzzle

# Specify map of directions
DIRECTIONS_MAP = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}
DIGIT_TO_LETTER_MAP = {
    0: "R",
    1: "D",
    3: "U",
    2: "L",
}


def parse_puzzle1(puzzle: str) -> list[tuple[int, int]]:
    new_node = (0, 0)
    vertices = []
    for line in puzzle.strip().splitlines():
        # Split line
        splits = line.strip().split(" ")
        letter = splits[0]
        count = int(splits[1])

        # Add vertices
        direction = DIRECTIONS_MAP[letter]
        new_node = (new_node[0] + count * direction[0], new_node[1] + count * direction[1])
        vertices.append(new_node)

    return vertices


def parse_puzzle2(puzzle: str) -> list[tuple[int, int]]:
    new_node = (0, 0)
    vertices = []
    for line in puzzle.strip().splitlines():
        # Split line
        splits = line.strip().split(" ")
        color = splits[2][2:-1]
        count = int(color[0:5], 16)  # converts hex str -> decimal
        letter = DIGIT_TO_LETTER_MAP[int(color[-1])]

        # Add vertices
        direction = DIRECTIONS_MAP[letter]
        new_node = (new_node[0] + count * direction[0], new_node[1] + count * direction[1])
        vertices.append(new_node)

    return vertices


def _polygon_area(edges: list[tuple[int, int]]) -> int:
    # https://stackoverflow.com/a/43659322
    area = 0
    for i in range(len(edges) - 1):
        x = edges[i + 1][0] - edges[i][0]
        y = edges[i + 1][1] + edges[i][1]
        area += x * y
    return area // 2


def _polygon_boundary(edges: list[tuple[int, int]]) -> int:
    # https://codeforces.com/blog/entry/65888
    num_edges = len(edges)
    boundary = num_edges
    for i in range(boundary):
        dx = edges[i][0] - edges[(i + 1) % num_edges][0]
        dy = edges[i][1] - edges[(i + 1) % num_edges][1]
        boundary += abs(gcd(dx, dy)) - 1
    return boundary


def picks_theorem(edges: list[tuple[int, int]]) -> int:
    # Uses Pick's Theorem: area = interior points + boundary points / 2 - 1
    area = _polygon_area(edges)
    boundary = _polygon_boundary(edges)
    interior = area + 1 - boundary // 2
    return interior + boundary


def solve_puzzle1(puzzle: str) -> int:
    edges = parse_puzzle1(puzzle)
    answer = picks_theorem(edges)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    edges = parse_puzzle2(puzzle)
    answer = picks_theorem(edges)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 46394
    assert solve_puzzle2(puzzle) == 201398068194715
