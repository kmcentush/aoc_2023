from aoc.day11 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
    """

    # Test helpers
    galaxies = p.parse_puzzle(puzzle, empty_scale=2)
    assert galaxies == [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
    distances = p.find_distances(galaxies)
    assert distances[(galaxies[4], galaxies[8])] == 9
    assert distances[(galaxies[0], galaxies[6])] == 15
    assert distances[(galaxies[2], galaxies[5])] == 17
    assert distances[(galaxies[7], galaxies[8])] == 5

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 374

    # Assert puzzle 2
    answer2 = p._solve_puzzle(puzzle, empty_scale=10)
    assert answer2 == 1030
    answer3 = p._solve_puzzle(puzzle, empty_scale=100)
    assert answer3 == 8410
