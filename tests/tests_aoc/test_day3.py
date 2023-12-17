from aoc.day3 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """

    # Test helpers
    matches = p._find_matches("..35..633.")
    assert matches == [(2, "35"), (6, "633")]

    # Assert puzzle 1
    symbols1 = p.extract_symbols(puzzle, p.VALID_SYMBOLS1)
    assert symbols1 == {
        (1, 3): [467, 35],
        (3, 6): [633],
        (4, 3): [617],
        (5, 5): [592],
        (8, 5): [755, 598],
        (8, 3): [664],
    }
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 4361

    # Assert puzzle 2
    symbols2 = p.extract_symbols(puzzle, p.VALID_SYMBOLS2)
    assert symbols2 == {(1, 3): [467, 35], (4, 3): [617], (8, 5): [755, 598]}
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 467835
