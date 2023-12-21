from collections import OrderedDict

from aoc.day15 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

    # Test helpers
    vals = p.parse_puzzle(puzzle)
    hashes = p.hash_vals(vals)
    boxes = p.get_boxes(vals)
    assert vals == ["rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9", "ab=5", "pc-", "pc=6", "ot=7"]
    assert hashes == [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]
    assert boxes == {0: OrderedDict([("rn", 1), ("cm", 2)]), 3: OrderedDict([("ot", 7), ("ab", 5), ("pc", 6)])}

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 1320

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 145
