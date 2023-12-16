import re
from collections import defaultdict

from aoc.utils import load_puzzle

# Compile patterns
DIGIT_PTRN = re.compile(r"\d+")
MAP_PTRN = re.compile(r"([\w-]+) map:")


def _explode_range(range_info: list[int], map_dict: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    destination_range_start, source_range_start, range_length = range_info
    map_dict[(destination_range_start, destination_range_start + range_length - 1)] = source_range_start
    return map_dict


def parse_puzzle(puzzle: str) -> tuple[list[tuple[int, int]], dict[str, dict[tuple[int, int], int]]]:
    puzzle = puzzle.strip()
    inverse_maps: dict[str, dict[tuple[int, int], int]] = defaultdict(lambda: {})
    for line in puzzle.splitlines():
        line_strip = line.strip()
        map_match = MAP_PTRN.match(line_strip)
        if line.startswith("seeds: "):
            seeds = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
            seed_pairs = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]
        elif map_match:
            map_type = map_match.group(1)
            map_type = "-".join(map_type.split("-")[::-1])
        elif line_strip != "":  # three digits
            range_info = [int(d) for d in DIGIT_PTRN.findall(line_strip)]
            inverse_maps[map_type] = _explode_range(range_info, inverse_maps[map_type])
    return seed_pairs, inverse_maps


def _lookup_map(key: int, inverse_map: dict[tuple[int, int], int]) -> int:
    for (destination_range_start, destination_range_end), source_range_start in inverse_map.items():
        if key >= destination_range_start and key <= destination_range_end:
            delta = key - destination_range_start
            return source_range_start + delta
    return key


def _valid_seed(seed: int, seed_pairs: list[tuple[int, int]]) -> bool:
    for seed_pair in seed_pairs:
        if seed >= seed_pair[0] and seed < seed_pair[0] + seed_pair[1]:  # [start_seed, end_seed)
            return True
    return False


def find_min_location(seed_pairs: list[tuple[int, int]], inverse_maps: dict[str, dict[tuple[int, int], int]]) -> int:
    location = 0
    while True:
        humidity = _lookup_map(location, inverse_maps["location-to-humidity"])
        temperature = _lookup_map(humidity, inverse_maps["humidity-to-temperature"])
        light = _lookup_map(temperature, inverse_maps["temperature-to-light"])
        water = _lookup_map(light, inverse_maps["light-to-water"])
        fertilizer = _lookup_map(water, inverse_maps["water-to-fertilizer"])
        soil = _lookup_map(fertilizer, inverse_maps["fertilizer-to-soil"])
        seed = _lookup_map(soil, inverse_maps["soil-to-seed"])
        if _valid_seed(seed, seed_pairs):
            break
        location += 1
    return location


def solve_puzzle(puzzle: str) -> int:
    seed_pairs, inverse_maps = parse_puzzle(puzzle)
    answer = find_min_location(seed_pairs, inverse_maps)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle(puzzle) == 81956384
