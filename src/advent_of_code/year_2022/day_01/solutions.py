from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 1: Calorie Counting ---"
PUZZLE_DIR = Path(__file__).parent


def load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def parse(puzzle_input: str) -> list[list[int]]:
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


def highest_total_calories(data: list[list[int]]) -> int:
    elves_total_calories: list[int] = [sum(calories) for calories in data]
    return max(elves_total_calories)


def main():
    print(PUZZLE_TITLE)
    puzzle_input: str = load_puzzle_input()
    data: list[list[int]] = parse(puzzle_input)

    answer_part_01: int = highest_total_calories(data)
    print(f"Answer for part 1: {answer_part_01}")


if __name__ == "__main__":
    main()
