import re
from copy import deepcopy
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 5: Supply Stacks ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text()


def _parse(puzzle_input: str) -> tuple[list[list[str]], list[dict]]:
    crates_input, rearrangement_input = puzzle_input.split("\n\n")

    crates_rows: list[list[str]] = _parse_crates_rows(crates_input)
    crate_stacks: list[list[str]] = _crate_stacks(crates_rows)

    rearrangement_steps: list[dict] = _parse_rearrangement_steps(
        rearrangement_input,
    )

    return crate_stacks, rearrangement_steps


def _parse_crates_rows(crates_input: str) -> list[list[str]]:
    stack_width: int = 4  # crate width plus space on right
    crates_rows: list[list[str]] = []
    for line in crates_input.splitlines()[:-1]:
        new_line = line + " "
        row: list[str] = [
            new_line[i : i + stack_width].strip()
            for i in range(0, len(new_line), stack_width)
        ]
        crates_rows.append(row)

    return crates_rows


def _crate_stacks(crates_rows: list[list[str]]) -> list[list[str]]:
    num_rows: int = len(crates_rows[-1])
    columns: list[list[str]] = [
        [row[i] for row in reversed(crates_rows)] for i in range(num_rows)
    ]
    crate_stacks = [[crate for crate in column if crate] for column in columns]
    return crate_stacks


def _parse_rearrangement_steps(rearrangement_input):
    num_crates_pat = re.compile(r"(?<=move\s)\d+")
    from_stack_pat = re.compile(r"(?<=from\s)\d+")
    to_stack_pat = re.compile(r"(?<=to\s)\d")

    rearrangement_steps: list[dict] = []
    for line in rearrangement_input.splitlines():
        num_crates_match = num_crates_pat.search(line)
        from_stack_match = from_stack_pat.search(line)
        to_stack_match = to_stack_pat.search(line)

        if (
            num_crates_match is not None
            and from_stack_match is not None
            and to_stack_match is not None
        ):
            num_crates: int = int(num_crates_match.group())
            from_stack: int = int(from_stack_match.group())
            to_stack: int = int(to_stack_match.group())

            rearrangement = {
                "num_crates": num_crates,
                "from_stack": from_stack,
                "to_stack": to_stack,
            }
            rearrangement_steps.append(rearrangement)

    return rearrangement_steps


def _rearrange_stacks(
    crate_stacks: list[list[str]],
    rearrangement_steps: list[dict],
    crane_model: str,
) -> list[list[str]]:
    new_stacks = deepcopy(crate_stacks)
    for step in rearrangement_steps:
        num_crates: int = step["num_crates"]
        from_stack_idx: int = step["from_stack"] - 1
        to_stack_idx: int = step["to_stack"] - 1

        moved_crates: list[str] = new_stacks[from_stack_idx][-num_crates:]

        del new_stacks[from_stack_idx][-num_crates:]
        if crane_model == "CrateMover 9000":
            new_stacks[to_stack_idx] += reversed(moved_crates)
        elif crane_model == "CrateMover 9001":
            new_stacks[to_stack_idx] += moved_crates

    return new_stacks


def _top_crates_message(stacks: list[list[str]]) -> str:
    top_crates = [stack[-1] for stack in stacks]
    return "".join(top_crates).replace("[", "").replace("]", "")


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    crate_stacks, rearrangement_steps = _parse(puzzle_input)

    rearranged_stacks_part1 = _rearrange_stacks(
        crate_stacks, rearrangement_steps, crane_model="CrateMover 9000"
    )
    print(f"Answer for part 1: {_top_crates_message(rearranged_stacks_part1)}")

    rearranged_stacks_part2 = _rearrange_stacks(
        crate_stacks, rearrangement_steps, crane_model="CrateMover 9001"
    )
    print(f"Answer for part 2: {_top_crates_message(rearranged_stacks_part2)}")


if __name__ == "__main__":
    main()
