from aoc.utils import load_puzzle
from tqdm.auto import tqdm

# Specify map of directions
DIRECTIONS_MAP = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}


def parse_puzzle(puzzle: str) -> tuple[list[tuple[int, int]], tuple[int, int]]:
    max_row, max_col = -1, -1
    min_row, min_col = 0, 0
    new_node = (0, 0)
    edges = [new_node]
    for line in puzzle.strip().splitlines():
        # Split line
        splits = line.strip().split(" ")
        letter = splits[0]
        count = int(splits[1])
        # color = splits[2]

        # Add edges
        direction = DIRECTIONS_MAP[letter]
        for _ in range(count):
            new_node = (new_node[0] + direction[0], new_node[1] + direction[1])
            if new_node[0] > max_row:
                max_row = new_node[0]
            if new_node[1] > max_col:
                max_col = new_node[1]
            if new_node[0] < min_row:
                min_row = new_node[0]
            if new_node[1] < min_col:
                min_col = new_node[1]
            edges.append(new_node)

    # Reset reference
    edges = [(e[0] - min_row, e[1] - min_col) for e in edges]

    return edges, (max_row + 1 - min_row, max_col + 1 - min_col)


def _is_inside(point: tuple[int, int], polygon: list[tuple[int, int]]):
    # Based on: https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    crosses = 0
    for i in range(len(polygon) - 1):
        poly1, poly2 = polygon[i], polygon[i + 1]
        if ((poly1[1] > point[1]) != (poly2[1] > point[1])) and (
            point[0] < (poly2[0] - poly1[0]) * (point[1] - poly1[1]) / (poly2[1] - poly1[1]) + poly1[0]
        ):
            crosses += 1

    return crosses % 2 == 1


def find_enclosed(edges: list[tuple[int, int]], size: tuple[int, int]) -> list[tuple[int, int]]:
    # Get all nodes not in the loop
    all_nodes = []
    for i in range(size[0]):
        for j in range(size[1]):
            all_nodes.append((i, j))
    maybe_enclosed = sorted(set(all_nodes) - set(edges))

    # Use ray tracing to determine if the node lies within the loop
    enclosed = []
    for node in tqdm(maybe_enclosed):
        if _is_inside(node, edges):
            enclosed.append(node)

    return enclosed


def solve_puzzle1(puzzle: str) -> int:
    edges, size = parse_puzzle(puzzle)
    enclosed = find_enclosed(edges, size)
    answer = len(set(edges)) + len(enclosed)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 46394
    # assert solve_puzzle2(puzzle) == 1067
