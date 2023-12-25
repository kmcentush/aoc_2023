import heapq

from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str) -> list[list[int]]:
    return [[int(col) for col in row.strip()] for row in puzzle.strip().splitlines()]


def minimal_heat(costs: list[list[int]], start: tuple[int, int], end: tuple[int, int], least: int, most: int) -> int:
    """This is a somewhat bruce-force approach."""
    num_rows = len(costs)
    num_cols = len(costs[0])
    queue = [(0, start, (0, 0))]
    seen = set()
    while queue:
        # Get setup
        total_heat, node, prev_direction = heapq.heappop(queue)

        # Break at destination; heap ensures minimal heat is processed first
        if node == end:
            return total_heat

        # Check if already seen
        if (node, prev_direction) in seen:
            continue
        seen.add((node, prev_direction))

        # Consider turning only
        for direction in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {
            prev_direction,
            (-prev_direction[0], -prev_direction[1]),
        }:
            # Move multiple times in a straight line after turning
            new_node, heat = node, total_heat
            for i in range(1, most + 1):
                new_node = new_node[0] + direction[0], new_node[1] + direction[1]
                if 0 <= new_node[0] < num_rows and 0 <= new_node[1] < num_cols:
                    heat += costs[new_node[0]][new_node[1]]
                    if i >= least:
                        heapq.heappush(queue, (heat, new_node, direction))

    return -1


def solve_puzzle1(puzzle: str) -> int:
    costs = parse_puzzle(puzzle)
    start = (0, 0)
    end = (len(costs) - 1, len(costs[0]) - 1)
    answer = minimal_heat(costs, start, end, least=1, most=3)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    costs = parse_puzzle(puzzle)
    start = (0, 0)
    end = (len(costs) - 1, len(costs[0]) - 1)
    answer = minimal_heat(costs, start, end, least=4, most=10)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 916
    assert solve_puzzle2(puzzle) == 1067
