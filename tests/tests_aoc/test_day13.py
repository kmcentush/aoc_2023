from aoc.day13 import puzzle as p


def test_puzzle():
    # Define puzzles
    puzzle = """
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.

        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#

        .#.##.#.#
        .##..##..
        .#.##.#..
        #......##
        #......##
        .#.##.#..
        .##..##.#

        #..#....#
        ###..##..
        .##.#####
        .##.#####
        ###..##..
        #..#....#
        #..##...#

        #.##..##.
        ..#.##.#.
        ##..#...#
        ##...#..#
        ..#.##.#.
        ..##..##.
        #.#.##.#.
    """

    # Test helpers
    games = p.parse_puzzle(puzzle)
    assert len(games) == 5
    assert len(games[0][0]) == 7  # game 1 rows
    assert len(games[0][1]) == 9  # game 1 columns
    row_mirrors, col_mirrors = p.find_mirrors(games, False)
    assert row_mirrors == [0, 4, 0, 3, 0]
    assert col_mirrors == [5, 0, 4, 0, 0]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 709

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 1400
