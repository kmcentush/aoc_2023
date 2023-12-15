import re

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"-?\d+")  # support negative numbers


def parse_puzzle(puzzle: str) -> list[list[int]]:
    puzzle = puzzle.strip()
    sequences = []
    for line in puzzle.splitlines():
        line_strip = line.strip()
        sequence = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
        sequences.append(sequence)
    return sequences


def _find_previous(sequence: list[int]) -> int:
    if all(s == 0 for s in sequence):
        return 0
    else:
        new_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        return new_sequence[0] - _find_previous(new_sequence)


def find_previous(sequences: list[list[int]]) -> list[int]:
    next_vals = []
    for sequence in sequences:
        next_val = sequence[0] - _find_previous(sequence)
        next_vals.append(next_val)
    return next_vals


def solve_puzzle(puzzle: str) -> int:
    sequences = parse_puzzle(puzzle)
    next_vals = find_previous(sequences)
    answer = sum(next_vals)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
