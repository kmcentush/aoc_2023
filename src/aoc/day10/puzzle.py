from collections import defaultdict
from copy import deepcopy

from aoc.utils import load_puzzle

# Define map of pipe to next steps
PIPE_MAP: dict[str, list[tuple[int, int]]] = {
    "S": [],
    ".": [],
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def _pipe_to_nodes(pipe: str, node: tuple[int, int]) -> list[tuple[int, int]]:
    return [(node[0] + step[0], node[1] + step[1]) for step in PIPE_MAP[pipe]]


def parse_puzzle(puzzle: str) -> tuple[tuple[int, int], dict[tuple[int, int], list[tuple[int, int]]]]:
    puzzle = puzzle.strip()
    graph: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    lines = puzzle.splitlines()
    for row, line in enumerate(lines):
        line_strip = line.strip()
        for col, pipe in enumerate(line_strip):
            node = (row, col)
            next_nodes = _pipe_to_nodes(pipe, node)
            if len(next_nodes) > 0:
                graph[node] += next_nodes
            if pipe == "S":
                start_node = node
    return start_node, graph


def _find_path(
    graph: dict[tuple[int, int], list[tuple[int, int]]], start_node: tuple[int, int], goal_node: tuple[int, int]
) -> list[tuple[int, int]]:
    # Use breadth-first-search
    explored = []
    queue = [[start_node]]
    while queue:
        # Get node
        path = queue.pop(0)
        node = path[-1]

        # OK to revisit nodes since we're checking both directions
        for next_node in graph[node]:
            # Don't go backwards
            if len(path) >= 2 and next_node == path[-2]:
                continue

            # Add node to path
            new_path = list(path)
            new_path.append(next_node)
            queue.append(new_path)

            # Break at goal
            if next_node == goal_node:
                return new_path

        # Mark node as visited
        explored.append(node)

    return []


def find_loop(start_node: tuple[int, int], graph: dict[tuple[int, int], list[tuple[int, int]]]):
    # Try S as all other types of pipes
    other_pipes = sorted(set(PIPE_MAP.keys()) - {"S", "."})
    loops = []
    for pipe in other_pipes:
        # Find loop
        graph_copy = deepcopy(graph)
        graph_copy[start_node] = _pipe_to_nodes(pipe, start_node)
        loop = _find_path(graph_copy, start_node, start_node)

        # Ensure second to last node in loop (i.e. last node before start node) legally connects to start
        if len(loop) > 0 and loop[-2] in graph_copy[start_node]:
            loops.append(loop)

    # Get longest loop
    if len(loops) > 0:
        loop_lengths = [len(v) for v in loops]
        max_idx = loop_lengths.index(max(loop_lengths))
        return loops[max_idx]

    return []


def solve_puzzle1(puzzle: str) -> int:
    start_node, graph = parse_puzzle(puzzle)
    loop = find_loop(start_node, graph)
    answer = len(loop) // 2
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 7086
