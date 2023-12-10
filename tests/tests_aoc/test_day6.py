from aoc.day6 import puzzle1 as p1
from aoc.day6 import puzzle2 as p2


def test_puzzle1():
    # Define puzzle
    puzzle = """
        Time:      7  15   30
        Distance:  9  40  200
    """

    # Assert
    times, distances = p1.parse_puzzle(puzzle)
    assert times == [7, 15, 30]
    assert distances == [9, 40, 200]
    numbers = p1.extract_numbers(times, distances)
    assert numbers == [4, 8, 9]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 288


def test_puzzle2():
    # Define puzzle
    puzzle = """
            Time:      7  15   30
            Distance:  9  40  200
        """

    # Assert
    time, distance = p2.parse_puzzle(puzzle)
    assert time == 71530
    assert distance == 940200
    answer = p2.solve_puzzle(puzzle)
    assert answer == 71503
