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
    vertices = p.parse_puzzle1(puzzle)
    assert vertices == [
        (0, 6),
        (5, 6),
        (5, 4),
        (7, 4),
        (7, 6),
        (9, 6),
        (9, 1),
        (7, 1),
        (7, 0),
        (5, 0),
        (5, 2),
        (2, 2),
        (2, 0),
        (0, 0),
    ]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 62

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 952408144115
