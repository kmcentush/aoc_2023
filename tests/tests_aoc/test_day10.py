from aoc.day10 import puzzle1 as p1

# from aoc.day10 import puzzle2 as p2


def test_puzzle1():
    # Define puzzles
    puzzle = """
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

    # Assert
    start_node, graph = p1.parse_puzzle(puzzle)
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
    loop = p1.find_loop(start_node, graph)
    assert loop == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1)]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 4
    answer2 = p1.solve_puzzle(puzzle2)
    assert answer2 == 8


# def test_puzzle2():
#     # Define puzzle
#     puzzle = """
#         0 3 6 9 12 15
#         1 3 6 10 15 21
#         10 13 16 21 30 45
#     """
#
#     # Assert
#     sequences = p2.parse_puzzle(puzzle)
#     next_vals = p2.find_previous(sequences)
#     assert next_vals == [-3, 0, 5]
#     answer = p2.solve_puzzle(puzzle)
#     assert answer == 2
