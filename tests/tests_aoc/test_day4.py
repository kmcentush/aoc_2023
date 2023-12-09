from aoc.day4 import puzzle1 as p1
from aoc.day4 import puzzle2 as p2


def test_puzzle1():
    # Assert helpers
    winning_numbers, card_numbers = p1._parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert winning_numbers == [41, 48, 83, 86, 17]
    assert card_numbers == [83, 86, 6, 31, 17, 9, 48, 53]

    # Define puzzle
    puzzle = """
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """

    # Assert
    numbers = p1.extract_numbers(puzzle)
    assert numbers == [8, 2, 2, 1]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 13


def test_puzzle2():
    # Assert helpers
    card_id, winning_numbers, card_numbers = p2._parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card_id == 1
    assert winning_numbers == [41, 48, 83, 86, 17]
    assert card_numbers == [83, 86, 6, 31, 17, 9, 48, 53]

    # Define puzzle
    puzzle = """
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """

    # Assert
    numbers = p2.extract_numbers(puzzle)
    assert numbers == {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
    answer = p2.solve_puzzle(puzzle)
    assert answer == 30
