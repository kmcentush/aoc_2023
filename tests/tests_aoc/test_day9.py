from aoc.day9 import puzzle as p


def test_puzzle():
    # Test helpers
    assert p.parse_puzzle("-5 6 7") == [[-5, 6, 7]]

    # Define puzzle
    puzzle = """
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
    """

    # Assert puzzle 1
    sequences = p.parse_puzzle(puzzle)
    assert sequences == [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
    next_vals = p.find_next(sequences)
    assert next_vals == [18, 28, 68]
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 114

    # Assert puzzle 2
    prev_vals = p.find_previous(sequences)
    assert prev_vals == [-3, 0, 5]
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 2
