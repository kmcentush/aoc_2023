from aoc.day7 import puzzle1 as p1
from aoc.day7 import puzzle2 as p2


def test_puzzle1():
    # Define puzzle
    puzzle = """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    """

    # Assert
    hands, bids = p1.parse_puzzle(puzzle)
    assert hands == ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
    assert bids == [765, 684, 28, 220, 483]
    ranks = p1.rank_hands(hands)
    assert ranks == [1, 4, 3, 2, 5]
    answer = p1.solve_puzzle(puzzle)
    assert answer == 6440


def test_puzzle2():
    # Define puzzle
    puzzle = """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    """

    # Assert
    hands, bids = p2.parse_puzzle(puzzle)
    assert hands == ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
    assert bids == [765, 684, 28, 220, 483]
    ranks = p2.rank_hands(hands)
    assert ranks == [1, 3, 2, 5, 4]
    answer = p2.solve_puzzle(puzzle)
    assert answer == 5905
