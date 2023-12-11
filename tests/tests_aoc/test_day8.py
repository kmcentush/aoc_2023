from aoc.day8 import puzzle1 as p1
from aoc.day8 import puzzle2 as p2


def test_puzzle1():
    # Test helpers
    dummy_puzzle = """
        RL

        AAA = (BBB, CCC)
        CCC = (ZZZ, GGG)
    """
    directions, maps = p1.parse_puzzle(dummy_puzzle)
    assert directions == [1, 0]
    assert maps == {
        "AAA": ("BBB", "CCC"),
        "CCC": ("ZZZ", "GGG"),
    }

    # Define puzzle
    puzzle = """
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)
    """

    # Assert
    answer = p1.solve_puzzle(puzzle)
    assert answer == 6


def test_puzzle2():
    # Define puzzle
    puzzle = """
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
    """

    # Assert
    answer = p2.solve_puzzle(puzzle)
    assert answer == 6
