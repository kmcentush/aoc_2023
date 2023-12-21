from collections import OrderedDict, defaultdict

from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str) -> list[str]:
    return puzzle.strip().split(",")


def _hash_val(val: str) -> int:
    hash = 0
    for c in val:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


def hash_vals(vals: list[str]) -> list[int]:
    return [_hash_val(v) for v in vals]


def get_boxes(vals: list[str]) -> dict[int, dict[str, int]]:
    # Loop over values
    boxes: dict[int, dict[str, int]] = defaultdict(OrderedDict)
    for val in vals:
        # Add or remove
        if "=" in val:
            key, lens = val.split("=")
            boxes[_hash_val(key)][key] = int(lens)  # will update in-place or insert at the end
        elif "-" in val:
            key = val.split("-")[0]
            box = boxes[_hash_val(key)]
            if key in box.keys():
                del box[key]

    return {k: v for k, v in boxes.items() if len(v) > 0}


def calculate_power(boxes: dict[int, dict[str, int]]) -> int:
    power = 0
    for box, vals in boxes.items():
        for slot, length in enumerate(vals.values()):
            power += (box + 1) * (slot + 1) * length
    return power


def solve_puzzle1(puzzle: str) -> int:
    vals = parse_puzzle(puzzle)
    hashes = hash_vals(vals)
    answer = sum(hashes)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    vals = parse_puzzle(puzzle)
    boxes = get_boxes(vals)
    answer = calculate_power(boxes)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 502139
    assert solve_puzzle2(puzzle) == 284132
