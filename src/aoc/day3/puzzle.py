import re
from collections import defaultdict

from aoc.utils import load_puzzle

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")

# Specify valid symbols
VALID_SYMBOLS1 = "#$%&*+-/=@"
VALID_SYMBOLS2 = "*"


def _find_matches(line: str) -> list[tuple[int, str]]:
    matches = []
    for match in DIGIT_PTRN.finditer(line):
        matches.append((match.start(), match.group()))
    return matches


def _is_symbol(row: int, col: int, puzzle_list: list[list[str]], valid_symbols: str) -> bool:
    if row < 0 or row > len(puzzle_list) - 1:
        return False
    if col < 0 or col > len(puzzle_list[0]) - 1:
        return False
    return puzzle_list[row][col] in valid_symbols


def extract_symbols(puzzle: str, valid_symbols: str) -> dict[tuple[int, int], list[int]]:
    # Find matches by row
    puzzle_list = []
    row_matches = []
    for line in puzzle.strip().splitlines():
        line_strip = line.strip()
        puzzle_list.append(list(line_strip))
        row_matches.append(_find_matches(line_strip))

    # Check nearby for symbols
    symbols = defaultdict(list)
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
                        check_row = row + i
                        check_col = col + j
                        is_symbol = _is_symbol(check_row, check_col, puzzle_list, valid_symbols)
                        if is_symbol:
                            near_symbol = True

            # Append
            if near_symbol:
                symbols[(check_row, check_col)].append(int(match_str))

    return symbols


def score_symbols2(symbols: dict[tuple[int, int], list[int]]) -> list[int]:
    # Check for valid gears
    numbers = []
    for gear_numbers in symbols.values():
        if len(gear_numbers) == 2:
            numbers.append(gear_numbers[0] * gear_numbers[1])
    return numbers


def solve_puzzle1(puzzle: str) -> int:
    symbols = extract_symbols(puzzle, VALID_SYMBOLS1)
    answer = sum([v for vs in symbols.values() for v in vs])
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    symbols = extract_symbols(puzzle, VALID_SYMBOLS2)
    numbers = score_symbols2(symbols)
    answer = sum(numbers)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 527144
    assert solve_puzzle2(puzzle) == 81463996
