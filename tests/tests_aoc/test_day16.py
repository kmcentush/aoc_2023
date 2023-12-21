from aoc.day16 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = r"""
        .|...\....
        |.-.\.....
        .....|-...
        ........|.
        ..........
        .........\
        ..../.\\..
        .-.-/..|..
        .|....-|.\
        ..//.|....
    """

    # Test helpers
    grid = p.parse_puzzle(puzzle)
    assert grid == [
        ".|...\\....",
        "|.-.\\.....",
        ".....|-...",
        "........|.",
        "..........",
        ".........\\",
        "..../.\\\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|....",
    ]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 46

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 51
