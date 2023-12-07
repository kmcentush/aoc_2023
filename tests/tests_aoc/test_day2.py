from aoc.day2 import puzzle1 as p1


def test_puzzle1():
    # Assert helpers
    game_id1, is_possible1 = p1._is_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    game_id2, is_possible2 = p1._is_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert game_id1 == 2
    assert is_possible1
    assert game_id2 == 3
    assert not is_possible2

    # Define puzzle
    puzzle = """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """

    # Assert
    numbers = p1.extract_numbers(puzzle)
    assert numbers == [1, 2, 5]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 8
