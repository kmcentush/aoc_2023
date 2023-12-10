from aoc.day5 import puzzle1 as p1
from aoc.day5 import puzzle2 as p2


def test_puzzle1():
    # Assert helpers
    map_dict = p1._explode_range([50, 98, 2], {})
    assert map_dict == {(98, 99): 50}

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

    # Assert
    seeds, maps = p1.parse_puzzle(puzzle)
    seeds_locations = p1.seeds_to_location(seeds, maps)
    assert seeds_locations == {79: 82, 14: 43, 55: 86, 13: 35}
    answer = p1.solve_puzzle(puzzle)
    assert answer == 35


def test_puzzle2():
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

    # Assert
    seed_pairs, inverse_maps = p2.parse_puzzle(puzzle)
    assert seed_pairs == [(79, 14), (55, 13)]
    answer = p2.solve_puzzle(puzzle)
    assert answer == 46
