from copy import deepcopy
from math import lcm

from aoc.utils import load_puzzle


def parse_puzzle(puzzle: str) -> tuple[dict[str, tuple[str, list[str]]], dict[str, dict[str, bool]]]:
    # Get modules
    modules: dict[str, tuple[str, list[str]]] = {}
    conjunction_memory: dict[str, dict[str, bool]] = {}
    for line in puzzle.strip().splitlines():
        line_strip = line.strip()
        module_str, destinations_str = line_strip.split(" -> ")
        destinations = destinations_str.split(", ")
        if module_str == "broadcaster":
            modules[module_str] = ("N/A", destinations)
        else:
            modules[module_str[1::]] = (module_str[0], destinations)
            if module_str[0] == "&":
                conjunction_memory[module_str[1::]] = {}

    # Index conjunction modules
    conjunction_memory_keys = set(conjunction_memory.keys())
    for module, (_, destinations) in modules.items():
        for destination in destinations:
            if destination in conjunction_memory_keys:
                conjunction_memory[destination][module] = False

    return modules, conjunction_memory


def _one_push(
    modules: dict[str, tuple[str, list[str]]],
    conjunction_memory: dict[str, dict[str, bool]],
    state: dict[str, bool],
    pulse_counts: dict[bool, int],
    break_pulse: tuple[str, bool] | None = None,
) -> tuple[dict[str, dict[str, bool]], dict[str, bool], dict[bool, int]]:
    # Start from the broadcaster
    pulse_counts[False] += 1  # count the button
    pulses = [("broadcaster", d, False) for d in modules["broadcaster"][1]]
    modules_keys = set(modules.keys())
    while len(pulses) > 0:
        # Get pulse metadata
        source, destination, pulse_type = pulses.pop(0)
        # print(source, f"-{'low' if not pulse_type else 'high'}->", destination)

        # Increment count
        pulse_counts[pulse_type] += 1

        # Break early via an exception
        if (source, pulse_type) == break_pulse:
            raise ValueError("Received break pulse.")

        # Handle destination
        if destination not in modules_keys:
            continue
        destination_type, new_destinations = modules[destination]

        # Update state
        if destination_type == "%":  # flip-flop
            if pulse_type:  # high
                continue  # do nothing
            state[destination] = not state[destination]
            new_pulse_type = state[destination]
        else:  # conjunction
            conjunction_memory[destination][source] = pulse_type
            new_pulse_type = not all(conjunction_memory[destination].values())

        # Send pulses
        pulses += [(destination, d, new_pulse_type) for d in new_destinations]

    return conjunction_memory, state, pulse_counts


def push(modules: dict[str, tuple[str, list[str]]], conjunction_memory: dict[str, dict[str, bool]], times: int) -> int:
    # Initialize state
    state = {k: False for k in modules.keys()}
    pulse_counts = {False: 0, True: 0}

    # Push
    for _ in range(times):
        conjunction_memory, state, pulse_counts = _one_push(modules, conjunction_memory, state, pulse_counts)

    return pulse_counts[False] * pulse_counts[True]


def push_until(
    modules: dict[str, tuple[str, list[str]]],
    original_conjunction_memory: dict[str, dict[str, bool]],
    target_conjunction: str,
) -> int:
    # Note that real problem's target is fired when `target_conjunction` does
    # Therefore we can just listen for the upstream modules to send a high pulse
    listen = list(original_conjunction_memory[target_conjunction].keys())

    # Push until we get a high pulse for the module we're listening to
    listen_pushes = []
    for module in listen:
        # Initialize state
        conjunction_memory = deepcopy(original_conjunction_memory)
        state = {k: False for k in modules.keys()}
        pulse_counts = {False: 0, True: 0}

        # Push
        pushes = 0
        try:
            while True:
                pushes += 1
                conjunction_memory, state, pulse_counts = _one_push(
                    modules, conjunction_memory, state, pulse_counts, break_pulse=(module, True)
                )
        except ValueError:
            listen_pushes.append(pushes)

    return lcm(*listen_pushes)


def solve_puzzle1(puzzle: str) -> int:
    modules, conjunction_memory = parse_puzzle(puzzle)
    answer = push(modules, conjunction_memory, times=1000)
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str, target_conjunction: str) -> int:
    modules, conjunction_memory = parse_puzzle(puzzle)
    answer = push_until(modules, conjunction_memory, target_conjunction)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 856482136
    assert solve_puzzle2(puzzle, "th") == 224046542165867  # "rx" only fires when "&th" does
