from aoc.day14 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
    """

    # Test helpers
    rows, cols = p.parse_puzzle(puzzle)
    assert len(rows) == 10
    assert len(cols) == 10
    assert rows[0] == "O....#...."
    assert cols[0] == "OO.O.O..##"
    assert cols[5] == "#.#..O#.##"
    assert rows == p._rotate(cols)
    assert cols == p._rotate(rows)
    rolled_rows1, rolled_cols1 = p.roll("N", rows, cols)
    assert rolled_cols1[0] == "OOOO....##"
    assert rolled_cols1[5] == "#.#O..#.##"
    rolled_rows2, rolled_cols2 = p.roll("S", rows, cols)
    assert rolled_cols2[0] == "....OOOO##"
    assert rolled_cols2[5] == "#.#..O#.##"
    rolled_rows3, rolled_cols3 = p.roll("W", rows, cols)
    assert rolled_rows3[0] == "O....#...."
    assert rolled_rows3[5] == "O.#O...#.#"
    rolled_rows4, rolled_cols4 = p.roll("E", rows, cols)
    assert rolled_rows4[0] == "....O#...."
    assert rolled_rows4[5] == ".O#...O#.#"

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 136

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 64
