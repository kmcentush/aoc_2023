from aoc.day21 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        ...........
        .....###.#.
        .###.##..#.
        ..#.#...#..
        ....#.#....
        .##..S####.
        .##..#...#.
        .......##..
        .##.#.####.
        .##..##.##.
        ...........
    """

    # Test helpers
    grid, start = p.parse_puzzle(puzzle)
    assert len(grid) == 11
    assert len(grid[1]) == 11
    assert start == (5, 5)

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle, 6)
    assert answer1 == 16

    # Assert puzzle 2
    answer21 = p.solve_puzzle2(puzzle, 5)
    answer22 = p.solve_puzzle2(puzzle, 16)
    assert answer21 == 13
    assert answer22 == 129
