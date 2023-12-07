from aoc.day1 import puzzle1 as p1
from aoc.day1 import puzzle2 as p2


def test_puzzle1():
    # Define puzzle
    puzzle = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    # Assert
    numbers = p1.extract_numbers(puzzle)
    assert numbers == [12, 38, 15, 77]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 142


def test_puzzle2():
    # Assert helpers
    digits_str = p2._str_to_digits("eightwo1three4")
    assert digits_str == "82134"

    # Define puzzle
    puzzle = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """

    # Assert
    numbers = p2.extract_numbers(puzzle)
    assert numbers == [29, 83, 13, 24, 42, 14, 76]
    answer = p2.solve_puzzle(puzzle)
    assert answer == 281
