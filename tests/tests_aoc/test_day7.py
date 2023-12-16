from aoc.day7 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    """

    # Test helpers
    hands, bids = p.parse_puzzle(puzzle)
    assert hands == ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
    assert bids == [765, 684, 28, 220, 483]

    # Assert puzzle 1
    hand_types1 = p.detect_hands1(hands)
    ranks1 = p.rank_hands(hands, hand_types1, p.CARD_CHARS1)
    assert ranks1 == [1, 4, 3, 2, 5]
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 6440

    # Assert puzzle 2
    hand_types2 = p.detect_hands2(hands)
    ranks2 = p.rank_hands(hands, hand_types2, p.CARD_CHARS2)
    assert ranks2 == [1, 3, 2, 5, 4]
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 5905
