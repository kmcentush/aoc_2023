from aoc.day18 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = r"""
        R 6 (#70c710)
        D 5 (#0dc571)
        L 2 (#5713f0)
        D 2 (#d2c081)
        R 2 (#59c680)
        D 2 (#411b91)
        L 5 (#8ceee2)
        U 2 (#caa173)
        L 1 (#1b58a2)
        U 2 (#caa171)
        R 2 (#7807d2)
        U 3 (#a77fa3)
        L 2 (#015232)
        U 2 (#7a21e3)
    """

    # Test helpers
    edges, size = p.parse_puzzle(puzzle)
    assert edges == [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (1, 6),
        (2, 6),
        (3, 6),
        (4, 6),
        (5, 6),
        (5, 5),
        (5, 4),
        (6, 4),
        (7, 4),
        (7, 5),
        (7, 6),
        (8, 6),
        (9, 6),
        (9, 5),
        (9, 4),
        (9, 3),
        (9, 2),
        (9, 1),
        (8, 1),
        (7, 1),
        (7, 0),
        (6, 0),
        (5, 0),
        (5, 1),
        (5, 2),
        (4, 2),
        (3, 2),
        (2, 2),
        (2, 1),
        (2, 0),
        (1, 0),
        (0, 0),
    ]
    assert size == (10, 7)

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 62

    # Assert puzzle 2
    # answer2 = p.solve_puzzle2(puzzle)
    # assert answer2 == 94
