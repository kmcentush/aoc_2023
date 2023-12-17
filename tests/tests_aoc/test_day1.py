from aoc.day1 import puzzle as p


def test_puzzle1():
    # Define puzzle
    puzzle1 = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """
    puzzle2 = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """

    # Test helpers
    digits_str = p._str_to_digits("eightwo1three4")
    assert digits_str == "82134"

    # Assert puzzle 1
    numbers1 = p.extract_numbers(puzzle1, convert_str=False)
    assert numbers1 == [12, 38, 15, 77]
    answer1 = p.solve_puzzle1(puzzle1)
    assert answer1 == 142

    # Assert puzzle 2
    numbers2 = p.extract_numbers(puzzle2, convert_str=True)
    assert numbers2 == [29, 83, 13, 24, 42, 14, 76]
    answer2 = p.solve_puzzle2(puzzle2)
    assert answer2 == 281
