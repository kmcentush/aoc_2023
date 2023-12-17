from aoc.day2 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """

    # Test helpers
    extract1 = p._extract_min_counts("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    extract2 = p._extract_min_counts("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert extract1 == (2, 1, 3, 4)
    assert extract2 == (3, 20, 13, 6)
    counts = p.extract_min_counts(puzzle)
    assert counts == {1: (4, 2, 6), 2: (1, 3, 4), 3: (20, 13, 6), 4: (14, 3, 15), 5: (6, 3, 2)}

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 8

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 2286
