from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 1: Calorie Counting ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str) -> list[list[int]]:
    puzzle_input_lines: list[str] = puzzle_input.splitlines()
    puzzle_input_lines.append("")

    data: list[list[int]] = []
    elf_food_calories: list[int] = []
    for line in puzzle_input_lines:
        if not line:
            data.append(elf_food_calories)
            elf_food_calories = []
        else:
            calories = int(line)
            elf_food_calories.append(calories)

    return data


def _total_calories_per_elf(data: list[list[int]]) -> list[int]:
    return [sum(calories) for calories in data]


def _highest_total_calories(total_calories_per_elf: list[int]) -> int:
    return max(total_calories_per_elf)


def _top_3_total_calories(total_calories_per_elf: list[int]) -> list[int]:
    return sorted(total_calories_per_elf)[-3:]


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input()
    data: list[list[int]] = _parse(puzzle_input)
    total_calories_per_elf: list[int] = _total_calories_per_elf(data)

    highest_total_calories: int = _highest_total_calories(
        total_calories_per_elf,
    )
    print(f"Answer for part 1: {highest_total_calories}")

    top_3_total_calories: list[int] = _top_3_total_calories(
        total_calories_per_elf,
    )
    print(f"Answer for part 2: {sum(top_3_total_calories)}")


if __name__ == "__main__":
    main()
