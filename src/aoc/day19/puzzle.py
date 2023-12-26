import re
from collections import defaultdict

from aoc.utils import load_puzzle

# Compile patterns
VALUES_PTRN = re.compile(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)")


def parse_puzzle(puzzle: str) -> tuple[dict[str, list[tuple[str, str, int, str] | str]], list[dict[str, int]]]:
    # Split puzzle
    workflows_str, parts_str = puzzle.strip().split("\n\n")

    # Handle workflows
    workflows: dict[str, list[tuple[str, str, int, str] | str]] = defaultdict(list)
    for line in workflows_str.splitlines():
        line_strip = line.strip()
        idx = line_strip.index("{")
        key = line_strip[0:idx]
        paths = line_strip[idx + 1 : -1].split(",")
        for path in paths:
            if ":" in path:
                rule, output = path.split(":")
                if "<" in rule:
                    letter, value = rule.split("<")
                    workflows[key].append((letter, "<", int(value), output))
                elif ">" in rule:
                    letter, value = rule.split(">")
                    workflows[key].append((letter, ">", int(value), output))
            else:
                workflows[key].append(path)

    # Parse parts
    parts = []
    for line in parts_str.splitlines():
        inputs = [int(i) for i in VALUES_PTRN.findall(line)[0]]
        parts.append(dict(zip("xmas", inputs, strict=True)))

    return workflows, parts


def _apply_workflow(workflow: list[tuple[str, str, int, str] | str], part: dict[str, int]) -> str:
    for path in workflow:
        if isinstance(path, tuple):
            key, operator, value, output = path
            if eval(f"{part[key]}{operator}{value}"):  # noqa: PGH001
                return output
        else:
            return path
    return ""


def apply_workflows(
    workflows: dict[str, list[tuple[str, str, int, str] | str]], parts: list[dict[str, int]]
) -> list[str]:
    results = []
    for part in parts:
        # Step through workflows
        next_workflow = "in"
        while next_workflow not in "AR":
            next_workflow = _apply_workflow(workflows[next_workflow], part)

        # Save result
        results.append(next_workflow)

    return results


def tree_workflows(
    workflows: dict[str, list[tuple[str, str, int, str] | str]],
) -> list[tuple[str, str, int] | tuple[str, str, int, str] | str]:
    # Path out all combinations
    approvals: list[tuple[str, str, int] | tuple[str, str, int, str] | str] = []
    queue = [["in"]]
    while len(queue) > 0:
        # Get key
        history = queue.pop(0)
        prev_rule = history[-1]
        if isinstance(prev_rule, tuple):
            key = prev_rule[-1]
        else:
            key = prev_rule

        # Break
        if key in "AR":
            if key == "A":
                approvals.append(history)  # type: ignore[arg-type]
            continue

        # Branch
        next_workflow = workflows[key]
        inv_next_workflow = []
        for i, rule in enumerate(next_workflow):
            if isinstance(rule, tuple):
                new_operator = ">=" if rule[1] == "<" else "<="
                inv_next_workflow.append((rule[0], new_operator, rule[2]))
            queue.append(history + inv_next_workflow[0:i] + [rule])  # type: ignore[arg-type, list-item]

    return approvals


def combinations(approvals: list[tuple[str, str, int] | tuple[str, str, int, str] | str]) -> int:
    # Keep rules that impact range
    paths = [[rule for rule in path if isinstance(rule, tuple)] for path in approvals]
    combinations = []
    for path in paths:
        limits = {
            "x": [1, 4000],
            "m": [1, 4000],
            "a": [1, 4000],
            "s": [1, 4000],
        }
        for rule in path:
            letter, operator, value = rule[0:3]
            # applies to range's max
            if operator == "<":  # applies to range's max
                limits[letter][1] = min([value - 1, limits[letter][1]])
            elif operator == "<=":
                limits[letter][1] = min([value, limits[letter][1]])
            # applies to range's min
            elif operator == ">":
                limits[letter][0] = max([value + 1, limits[letter][0]])
            elif operator == ">=":
                limits[letter][0] = max([value, limits[letter][0]])

        # Calculate combinations
        combinations.append(
            (limits["x"][1] - limits["x"][0] + 1)
            * (limits["m"][1] - limits["m"][0] + 1)
            * (limits["a"][1] - limits["a"][0] + 1)
            * (limits["s"][1] - limits["s"][0] + 1)
        )

    return sum(combinations)


def solve_puzzle1(puzzle: str) -> int:
    workflows, parts = parse_puzzle(puzzle)
    results = apply_workflows(workflows, parts)
    answer = sum([sum(parts[i].values()) for i in range(len(results)) if results[i] == "A"])
    print(f"Answer: {answer}")
    return answer


def solve_puzzle2(puzzle: str) -> int:
    workflows, _ = parse_puzzle(puzzle)
    approvals = tree_workflows(workflows)
    answer = combinations(approvals)
    print(f"Answer: {answer}")
    return answer


if __name__ == "__main__":  # pragma: no cover
    puzzle = load_puzzle("puzzle.txt")
    assert solve_puzzle1(puzzle) == 353553
    assert solve_puzzle2(puzzle) == 124615747767410
