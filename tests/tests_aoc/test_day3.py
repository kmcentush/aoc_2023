from aoc.day3 import puzzle1 as p1
from aoc.day3 import puzzle2 as p2


def test_puzzle1():
    # Assert helpers
    matches = p1._find_matches("..35..633.")
    assert matches == [(2, "35"), (6, "633")]

    # Define puzzle
    puzzle = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """

    # Assert
    numbers = p1.extract_numbers(puzzle)
    assert numbers == [467, 35, 633, 617, 592, 755, 664, 598]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 4361


def test_puzzle2():
    # Define puzzle
    puzzle = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """

    # Assert
    numbers = p2.extract_numbers(puzzle)
    assert numbers == [16345, 451490]
    answer = p2.solve_puzzle(puzzle)
    assert answer == 467835
