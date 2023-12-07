from aoc.day1.puzzle1 import extract_numbers, solve_puzzle


def test_puzzle1():
    # Define puzzle
    puzzle = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    # Assert
    numbers = extract_numbers(puzzle)
    assert numbers == [12, 38, 15, 77]
    answer = solve_puzzle(puzzle)
    assert answer == 142
