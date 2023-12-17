from aoc.day12 import puzzle as p


def test_puzzle():
    # Define puzzles
    puzzle = """
        ???.### 1,1,3
        .??..??...?##. 1,1,3
        ?#?#?#?#?#?#?#? 1,3,1,6
        ????.#...#... 4,1,1
        ????.######..#####. 1,6,5
        ?###???????? 3,2,1
    """

    # Test helpers
    lines = p.parse_puzzle(puzzle)
    assert lines == [
        ("???.###", (1, 1, 3)),
        (".??..??...?##.", (1, 1, 3)),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6)),
        ("????.#...#...", (4, 1, 1)),
        ("????.######..#####.", (1, 6, 5)),
        ("?###????????", (3, 2, 1)),
    ]
    arrangements1 = p._find_arrangements("???.###", (1, 1, 3))
    assert arrangements1 == 1
    arrangements2 = p._find_arrangements("?###????????", (3, 2, 1))
    assert arrangements2 == 10

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 21

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 525152
