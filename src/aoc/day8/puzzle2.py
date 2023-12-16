import itertools
import math
import re
from collections import defaultdict

from aoc.utils import load_puzzle

# Compile patterns
MAP_PTRN = re.compile(r"(\w+) = \((\w+), (\w+)\)")


def parse_puzzle(puzzle: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    maps = {}
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        line_strip = line.strip()
        map_match = MAP_PTRN.match(line_strip)
        if map_match:
            key, left, right = map_match.groups()
            maps[key] = (left, right)
        elif line_strip != "":
            directions = [0 if d == "L" else 1 for d in line_strip]
    return directions, maps


def navigate(directions: list[int], maps: dict[str, tuple[str, str]]):
    # Look for cycles
    num_directions = len(directions)
    locations = [k for k in maps.keys() if k.endswith("A")]
    steps_to_z = defaultdict(list)
    for start_location in locations:
        directions_idx = 0
        steps = 0
        location = start_location
        visited_locations = []
        while (directions_idx, location) not in visited_locations:  # will break at a cycle
            # Mark visited
            visited_locations.append((directions_idx, location))

            # Maybe loop directions index
            if directions_idx > num_directions - 1:
                directions_idx = 0
            direction = directions[directions_idx]

            # Step
            location = maps[location][direction]
            directions_idx += 1
            steps += 1

            # Mark Zs
            if location.endswith("Z"):
                steps_to_z[start_location].append(steps)

    # Find the LCMs of all combinations of Z
    combinations = list(itertools.product(*steps_to_z.values()))
    lcms = [math.lcm(*combination) for combination in combinations]
    return min(lcms)


def solve_puzzle(puzzle: str) -> int:
    directions, maps = parse_puzzle(puzzle)
    answer = navigate(directions, maps)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 13663968099527
