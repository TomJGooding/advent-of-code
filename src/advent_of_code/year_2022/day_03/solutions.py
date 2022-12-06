import string
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 3: Rucksack Reorganization ---"
PUZZLE_DIR = Path(__file__).parent


ITEMS: str = string.ascii_letters


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str, puzzle_part: int) -> list[tuple]:
    data: list[tuple] = []
    puzzle_input_lines: list[str] = puzzle_input.splitlines()

    if puzzle_part == 1:
        for line in puzzle_input_lines:
            half_length: int = len(line) // 2
            compartment_1: str = line[:half_length]
            compartment_2: str = line[half_length:]
            rucksack: tuple = compartment_1, compartment_2
            data.append(rucksack)

    elif puzzle_part == 2:
        group_size: int = 3
        for i in range(0, len(puzzle_input_lines), group_size):
            elf_group = puzzle_input_lines[i : i + group_size]
            data.append(tuple(elf_group))

    return data


def _common_item(items_group: tuple) -> str:
    common = list(set.intersection(*map(set, items_group)))
    return common[0]


def _priority(item: str) -> int:
    return ITEMS.index(item) + 1


def _common_items_priorities(data: list[tuple]) -> list[int]:
    result: list[int] = []
    for items_group in data:
        common_item: str = _common_item(items_group)
        item_priority: int = _priority(common_item)
        result.append(item_priority)

    return result


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input()

    data_part_1: list[tuple] = _parse(puzzle_input, puzzle_part=1)
    print(f"Answer for part 1: {sum(_common_items_priorities(data_part_1))}")

    data_part_2: list[tuple] = _parse(puzzle_input, puzzle_part=2)
    print(f"Answer for part 1: {sum(_common_items_priorities(data_part_2))}")


if __name__ == "__main__":
    main()
