from collections import Counter

from aoc.utils import load_puzzle

# Specify cards in descending rank order
CARD_CHARS = "AKQJT98765432"


def parse_puzzle(puzzle: str) -> tuple[list[str], list[int]]:
    hands = []
    bids = []
    puzzle = puzzle.strip()
    for line in puzzle.splitlines():
        line_strip = line.strip()
        split = line_strip.split(" ")
        hand = split[0]
        bid = int(split[1])
        hands.append(hand)
        bids.append(bid)
    return hands, bids


def _break_ties(hands: list[str], out: list[str], hand_idx: int = 0) -> list[str]:
    for char in CARD_CHARS:
        starts_with = []
        for hand in hands:
            if hand[hand_idx] == char:
                starts_with.append(hand)
        num_starts_with = len(starts_with)
        if num_starts_with > 1:
            _break_ties(starts_with, out, hand_idx=hand_idx + 1)  # modifies inplace
        elif num_starts_with == 1:
            out.append(starts_with[0])
    return out


def rank_hands(hands: list[str]) -> list[int]:
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
    hand_types = {k: v for k, v in hand_types.items() if len(v) > 0}  # remove empty hand types

    # Assign ranks
    ranks_lookup = []
    for hand_type_hands in hand_types.values():
        if len(hand_type_hands) > 1:
            ranks_lookup += _break_ties(hand_type_hands, [])
        else:
            ranks_lookup.append(hand_type_hands[0])
    ranks_lookup = ranks_lookup[::-1]  # reverse so first index is lowest rank
    ranks = [ranks_lookup.index(h) + 1 for h in hands]
    return ranks


def solve_puzzle(puzzle: str) -> int:
    hands, bids = parse_puzzle(puzzle)
    ranks = rank_hands(hands)
    answer = 0
    for i in range(len(bids)):
        answer += bids[i] * ranks[i]
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 248559379