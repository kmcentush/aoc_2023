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
    puzzle3 = """
        .F----7F7F7F7F-7....
        .|F--7||||||||FJ....
        .||.FJ||||||||L7....
        FJL7L7LJLJ||LJ.L-7..
        L--J.L7...LJS7F-7L7.
        ....F-J..F7FJ|L7L7L7
        ....L7.F7||L7|.L7L7|
        .....|FJLJ|FJ|F7|.LJ
        ....FJL-7.||.||||...
        ....L---J.LJ.LJLJ...
    """
    puzzle4 = """
        FF7FSF7F7F7F7F7F---7
        L|LJ||||||||||||F--J
        FL-7LJLJ||||||LJL-77
        F--JF--7||LJLJ7F7FJ-
        L---JF-JLJ.||-FJLJJ7
        |F|F-JF---7F7-L7L|7|
        |FFJF7L7F-JF7|JL---7
        7-L-JL7||F7|L7F-7F7|
        L.L7LFJ|||||FJL7||LJ
        L7JLJL-JLJLJL--JLJ.L
    """

    # Test helpers
    start_node, graph, grid_size = p.parse_puzzle(puzzle1)
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
    assert grid_size == (5, 5)
    loop = p.find_loop(start_node, graph)
    assert loop == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1)]
    enclosed = p.find_enclosed(loop, grid_size)
    assert enclosed == [(2, 2)]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle1)
    assert answer1 == 4
    answer2 = p.solve_puzzle1(puzzle2)
    assert answer2 == 8

    # Assert puzzle 2
    # answer3 = p.solve_puzzle2(puzzle1)
    # assert answer3 == 1
    # answer4 = p.solve_puzzle2(puzzle2)
    # assert answer4 == 1
    answer5 = p.solve_puzzle2(puzzle3)
    assert answer5 == 8
    answer6 = p.solve_puzzle2(puzzle4)
    assert answer6 == 10
