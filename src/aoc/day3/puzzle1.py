import re

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")


def _find_matches(line: str) -> list[tuple[int, str]]:
    matches = []
    for match in DIGIT_PTRN.finditer(line):
        matches.append((match.start(), match.group()))
    return matches


def _is_symbol(row: int, col: int, puzzle_list: list[list[str]]) -> bool:
    if row < 0 or row > len(puzzle_list) - 1:
        return False
    if col < 0 or col > len(puzzle_list[0]) - 1:
        return False
    char = puzzle_list[row][col]
    return char != "." and not char.isdigit()


def extract_numbers(puzzle: str) -> list[int]:
    # Prepare to extract
    numbers = []
    puzzle = puzzle.strip()

    # Find matches by row
    puzzle_list = []
    row_matches = []
    for line in puzzle.splitlines():
        line_strip = line.strip()
        puzzle_list.append(list(line_strip))
        row_matches.append(_find_matches(line_strip))

    # Check nearby for symbols
    for row, matches in enumerate(row_matches):
        for match in matches:
            # Get info
            start_col = match[0]
            match_str = match[1]

            # Check all 8 locations around character
            near_symbol = False
            for col in range(start_col, start_col + len(match_str)):
                # Maybe break early
                if near_symbol:
                    break

                for i in range(-1, 2):
                    # Maybe break early
                    if near_symbol:
                        break

                    for j in range(-1, 2):
                        # Maybe break early
                        if near_symbol:
                            break

                        # Check
                        is_symbol = _is_symbol(row + i, col + j, puzzle_list)
                        if is_symbol:
                            near_symbol = True

            # Append
            if near_symbol:
                numbers.append(int(match_str))

    return numbers


def solve_puzzle(puzzle: str) -> int:
    numbers = extract_numbers(puzzle)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
