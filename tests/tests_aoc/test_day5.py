from aoc.day5 import puzzle as p


def test_puzzle():
    # Define puzzle
    puzzle = """
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
    """

    # Test helpers
    seeds, maps = p.parse_puzzle1(puzzle)
    seeds_locations = p.seeds_to_location(seeds, maps)
    assert seeds_locations == {79: 82, 14: 43, 55: 86, 13: 35}
    seed_pairs, inverse_maps = p.parse_puzzle2(puzzle)
    assert seed_pairs == [(79, 14), (55, 13)]

    # Assert puzzle 1
    answer1 = p.solve_puzzle1(puzzle)
    assert answer1 == 35

    # Assert puzzle 2
    answer2 = p.solve_puzzle2(puzzle)
    assert answer2 == 46
