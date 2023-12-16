from aoc.day10 import puzzle as p


def test_puzzle():
    # Define puzzles
    puzzle1 = """
        .....
        .S-7.
        .|.|.
        .L-J.
        .....
    """
    puzzle2 = """
        7-F7-
        .FJ|7
        SJLL7
        |F--J
        LJ.LJ
    """

    # Test helpers
    start_node, graph = p.parse_puzzle(puzzle1)
    assert start_node == (1, 1)
    assert graph == {
        (1, 2): [(1, 3), (1, 1)],
        (1, 3): [(2, 3), (1, 2)],
        (2, 1): [(1, 1), (3, 1)],
        (2, 3): [(1, 3), (3, 3)],
        (3, 1): [(2, 1), (3, 2)],
        (3, 2): [(3, 3), (3, 1)],
        (3, 3): [(2, 3), (3, 2)],
    }
    loop = p.find_loop(start_node, graph)
    assert loop == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1)]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle1)
    assert answer1 == 4
    answer2 = p.solve_puzzle1(puzzle2)
    assert answer2 == 8
