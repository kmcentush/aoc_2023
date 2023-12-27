from aoc.day20 import puzzle as p


def test_puzzle():
    # Define puzzles
    puzzle1 = """
        broadcaster -> a, b, c
        %a -> b
        %b -> c
        %c -> inv
        &inv -> a
    """
    puzzle2 = """
        broadcaster -> a
        %a -> inv, con
        &inv -> b
        %b -> con
        &con -> output
    """
    puzzle3 = """
        broadcaster -> a, b
        %a -> con
        %b -> con
        &con -> output
    """

    # Test helpers
    modules1, conjunction_memory1 = p.parse_puzzle(puzzle1)
    assert modules1 == {
        "a": ("%", ["b"]),
        "b": ("%", ["c"]),
        "broadcaster": ("N/A", ["a", "b", "c"]),
        "c": ("%", ["inv"]),
        "inv": ("&", ["a"]),
    }
    assert conjunction_memory1 == {"inv": {"c": False}}

    # Assert puzzle 1
    answer11 = p.solve_puzzle1(puzzle1)
    answer12 = p.solve_puzzle1(puzzle2)
    assert answer11 == 32000000
    assert answer12 == 11687500

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle3, "con")
    assert answer2 == 1
