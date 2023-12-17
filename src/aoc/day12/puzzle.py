import re

from aoc.utils import load_puzzle

# Compile patterns
DIGIT_PTRN = re.compile(r"(\d+)")


def parse_puzzle(puzzle: str) -> list[tuple[str, list[int]]]:
    lines = []
    for line in puzzle.strip().splitlines():
        split = line.strip().split(" ")
        counts = [int(d) for d in DIGIT_PTRN.findall(split[1])]
        lines.append((split[0], counts))
    return lines


def _count_arrangement(line: str) -> list[int]:
    splits = line.replace(".", " ").split()
    return [len(s) for s in splits]


def _next_paths(path: str, line: str) -> list[str]:
    path_len = len(path)
    remaining = line[path_len::]
    if "?" in remaining:
        idx = remaining.index("?")
        prefix = path + remaining[0:idx]
        return [prefix + "#", prefix + "."]
    return [path + remaining]


def _find_arrangements(line: str, counts: list[int]) -> list[str]:
    # Use breadth-first-search
    arrangements = []
    line_len = len(line)
    counts_len = len(counts)
    explored = []
    queue = _next_paths("", line)
    while queue:
        # Get node
        path = queue.pop(0)

        # Don't revisit nodes nor explore longer paths
        if path in explored:
            continue

        # Get next node(s)
        next_paths = _next_paths(path, line)
        for next_path in next_paths:
            # Ensure still possibly correct
            next_path_len = len(next_path)
            next_counts = _count_arrangement(next_path)  # need to count next_path
            next_counts_len = len(next_counts)
            if next_counts_len > counts_len:  # too many groups
                continue
            elif next_counts_len < counts_len and next_path_len < line_len:  # earlier groups too long
                should_continue = False
                for i in range(next_counts_len):
                    if next_counts[i] > counts[i]:
                        should_continue = True
                        break
                if should_continue:
                    continue

            # Maybe add path to queue
            if next_path_len < line_len:
                queue.append(next_path)

            # Include if correct
            if next_path_len == line_len and next_counts == counts:
                arrangements.append(next_path)

        # Mark node as explored
        explored.append(path)

    return arrangements


def find_arrangements(lines: list[tuple[str, list[int]]]) -> list[list[str]]:
    arrangements = []
    for line, digits in lines:
        arrangements.append(_find_arrangements(line, digits))
    return arrangements


def _solve_puzzle(puzzle: str, copies: int) -> int:
    lines = parse_puzzle(puzzle)
    # TODO: use `copies` and be smart; all but last group of original pattern won't change
    arrangements = find_arrangements(lines)
    answer = sum([len(a) for a in arrangements])
    print(f"Answer: {answer}")
    return answer


def solve_puzzle1(puzzle: str) -> int:
    return _solve_puzzle(puzzle, copies=1)


def solve_puzzle2(puzzle: str) -> int:
    return _solve_puzzle(puzzle, copies=5)


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 7379
    # assert solve_puzzle2(puzzle) == 731244261352