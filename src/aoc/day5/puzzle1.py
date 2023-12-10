import re
from collections import defaultdict

from aoc.utils import multiline_input

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")
MAP_PTRN = re.compile(r"([\w-]+) map:")


def _explode_range(range_info: list[int], map_dict: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    destination_range_start, source_range_start, range_length = range_info
    map_dict[(source_range_start, source_range_start + range_length - 1)] = destination_range_start
    return map_dict


def parse_puzzle(puzzle: str) -> tuple[list[int], dict[str, dict[tuple[int, int], int]]]:
    puzzle = puzzle.strip()
    maps: dict[str, dict[tuple[int, int], int]] = defaultdict(lambda: {})
    for line in puzzle.splitlines():
        line_strip = line.strip()
        map_match = MAP_PTRN.match(line_strip)
        if line.startswith("seeds: "):
            seeds = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
        elif map_match:
            map_type = map_match.group(1)
        elif line_strip != "":  # three digits
            range_info = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
            maps[map_type] = _explode_range(range_info, maps[map_type])
    return seeds, maps


def _lookup_map(key: int, map: dict[tuple[int, int], int]) -> int:
    for (source_range_start, source_range_end), destination_range_start in map.items():
        if key >= source_range_start and key <= source_range_end:
            delta = key - source_range_start
            return destination_range_start + delta
    return key


def seeds_to_location(seeds: list[int], maps: dict[str, dict[tuple[int, int], int]]) -> dict[int, int]:
    out = {}
    for seed in seeds:
        soil = _lookup_map(seed, maps["seed-to-soil"])
        fertilizer = _lookup_map(soil, maps["soil-to-fertilizer"])
        water = _lookup_map(fertilizer, maps["fertilizer-to-water"])
        light = _lookup_map(water, maps["water-to-light"])
        temperature = _lookup_map(light, maps["light-to-temperature"])
        humidity = _lookup_map(temperature, maps["temperature-to-humidity"])
        location = _lookup_map(humidity, maps["humidity-to-location"])
        out[seed] = location
    return out


def solve_puzzle(puzzle: str) -> int:
    seeds, maps = parse_puzzle(puzzle)
    seeds_locations = seeds_to_location(seeds, maps)
    answer = min(seeds_locations.values())
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = multiline_input()
    solve_puzzle(puzzle)
