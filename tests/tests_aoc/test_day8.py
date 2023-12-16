from aoc.day8 import puzzle as p


def test_puzzle():
    # Define puzzles
    puzzle1 = """
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)
    """
    puzzle2 = """
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
    puzzle3 = """
        LRL

        11A = (11B, XXX)
        11B = (11Z, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
    """

    # Test helpers
    directions, maps = p.parse_puzzle(puzzle1)
    assert directions == [0, 0, 1]
    assert maps == {"AAA": ("BBB", "BBB"), "BBB": ("AAA", "ZZZ"), "ZZZ": ("ZZZ", "ZZZ")}

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle1)
    assert answer1 == 6

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle2)
    answer3 = p.solve_puzzle2(puzzle3)
    assert answer2 == 6
    assert answer3 == 6
