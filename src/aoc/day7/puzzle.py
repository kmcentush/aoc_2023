from collections import Counter

from aoc.utils import load_puzzle

# Specify cards in descending rank order
CARD_CHARS1 = "AKQJT98765432"
CARD_CHARS2 = "AKQT98765432J"


def parse_puzzle(puzzle: str) -> tuple[list[str], list[int]]:
    hands = []
    bids = []
    for line in puzzle.strip().splitlines():
        line_strip = line.strip()
        split = line_strip.split(" ")
        hand = split[0]
        bid = int(split[1])
        hands.append(hand)
        bids.append(bid)
    return hands, bids


def _break_ties(hands: list[str], out: list[str], card_chars: str, hand_idx: int = 0) -> list[str]:
    for char in card_chars:
        starts_with = []
        for hand in hands:
            if hand[hand_idx] == char:
                starts_with.append(hand)
        num_starts_with = len(starts_with)
        if num_starts_with > 1:
            _break_ties(starts_with, out, card_chars, hand_idx=hand_idx + 1)  # modifies inplace
        elif num_starts_with == 1:
            out.append(starts_with[0])
    return out


def detect_hands1(hands: list[str]) -> dict[str, list[str]]:
    # Detect hand types
    hand_types: dict[str, list[str]] = {  # keys enforce rank order
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two": [],
        "one": [],
        "high": [],
    }
    for hand in hands:
        counts = Counter(hand)
        num_kind1 = counts.most_common()[0][1]
        if num_kind1 != 5:
            num_kind2 = counts.most_common()[1][1]
        else:
            num_kind2 = 0
        if num_kind1 == 5:
            hand_types["five"].append(hand)
        elif num_kind1 == 4:
            hand_types["four"].append(hand)
        elif num_kind1 == 3 and num_kind2 == 2:
            hand_types["full"].append(hand)
        elif num_kind1 == 3:
            hand_types["three"].append(hand)
        elif num_kind1 == 2 and num_kind2 == 2:
            hand_types["two"].append(hand)
        elif num_kind1 == 2:
            hand_types["one"].append(hand)
        else:
            hand_types["high"].append(hand)

    return {k: v for k, v in hand_types.items() if len(v) > 0}  # remove empty hand types


def detect_hands2(hands: list[str]) -> dict[str, list[str]]:
    # Detect hand types
    hand_types: dict[str, list[str]] = {  # keys enforce rank order
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two": [],
        "one": [],
        "high": [],
    }
    hand_type_keys = list(hand_types.keys())
    for hand in hands:
        # Try all combos of J -> other char and keep the best
        best_hand_type = "high"  # start with worst hand type
        for char in CARD_CHARS2:
            # Determine hand type
            hand_joker = hand.replace("J", char)
            counts = Counter(hand_joker)
            num_kind1 = counts.most_common()[0][1]
            if num_kind1 != 5:
                num_kind2 = counts.most_common()[1][1]
            else:
                num_kind2 = 0
            if num_kind1 == 5:
                hand_type = "five"
            elif num_kind1 == 4:
                hand_type = "four"
            elif num_kind1 == 3 and num_kind2 == 2:
                hand_type = "full"
            elif num_kind1 == 3:
                hand_type = "three"
            elif num_kind1 == 2 and num_kind2 == 2:
                hand_type = "two"
            elif num_kind1 == 2:
                hand_type = "one"
            else:
                hand_type = "high"

            # Update if better than previous best
            if hand_type_keys.index(hand_type) < hand_type_keys.index(best_hand_type):
                best_hand_type = hand_type

        # Save hand type
        hand_types[best_hand_type].append(hand)

    return {k: v for k, v in hand_types.items() if len(v) > 0}  # remove empty hand types


def rank_hands(hands: list[str], hand_types: dict[str, list[str]], card_chars: str) -> list[int]:
    ranks_lookup = []
    for hand_type_hands in hand_types.values():
        if len(hand_type_hands) > 1:
            ranks_lookup += _break_ties(hand_type_hands, [], card_chars)
        else:
            ranks_lookup.append(hand_type_hands[0])
    ranks_lookup = ranks_lookup[::-1]  # reverse so first index is lowest rank
    return [ranks_lookup.index(h) + 1 for h in hands]


def solve_puzzle1(puzzle: str) -> int:
    hands, bids = parse_puzzle(puzzle)
    hand_types = detect_hands1(hands)
    ranks = rank_hands(hands, hand_types, CARD_CHARS1)
    answer = 0
    for i in range(len(bids)):
        answer += bids[i] * ranks[i]
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    hands, bids = parse_puzzle(puzzle)
    hand_types = detect_hands2(hands)
    ranks = rank_hands(hands, hand_types, CARD_CHARS2)
    answer = 0
    for i in range(len(bids)):
        answer += bids[i] * ranks[i]
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 248559379
    assert solve_puzzle2(puzzle) == 249631254
