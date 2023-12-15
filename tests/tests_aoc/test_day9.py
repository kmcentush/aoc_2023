from aoc.day9 import puzzle1 as p1
from aoc.day9 import puzzle2 as p2


def test_puzzle1():
    # Test helpers
    assert p1.parse_puzzle("-5 6 7") == [[-5, 6, 7]]

    # Define puzzle
    puzzle = """
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
    """

    # Assert
    sequences = p1.parse_puzzle(puzzle)
    assert sequences == [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
    next_vals = p1.find_next(sequences)
    assert next_vals == [18, 28, 68]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 114


def test_puzzle2():
    # Define puzzle
    puzzle = """
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
    """

    # Assert
    sequences = p2.parse_puzzle(puzzle)
    next_vals = p2.find_previous(sequences)
    assert next_vals == [-3, 0, 5]
    answer = p2.solve_puzzle(puzzle)
    assert answer == 2
