from aoc.day6 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        Time:      7  15   30
        Distance:  9  40  200
    """

    # Test helpers
    times1, distances1 = p.parse_puzzle1(puzzle)
    assert times1 == [7, 15, 30]
    assert distances1 == [9, 40, 200]
    numbers1 = p.extract_numbers(times1, distances1)
    assert numbers1 == [4, 8, 9]
    times2, distances2 = p.parse_puzzle2(puzzle)
    assert times2 == [71530]
    assert distances2 == [940200]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 288

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 71503
