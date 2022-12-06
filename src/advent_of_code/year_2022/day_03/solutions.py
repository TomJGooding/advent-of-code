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


def _parse(puzzle_input: str) -> list[tuple]:
    data: list[tuple] = []
    for line in puzzle_input.splitlines():
        half_length: int = len(line) // 2
        compartment_1: str = line[:half_length]
        compartment_2: str = line[half_length:]
        rucksack: tuple = compartment_1, compartment_2
        data.append(rucksack)

    return data


def _common_item(compartment_1, compartment_2) -> str:
    common = list(set(compartment_1) & set(compartment_2))
    return common[0]


def _priority(item: str) -> int:
    return ITEMS.index(item) + 1


def _common_items_priorities(data: list[tuple]) -> list[int]:
    result: list[int] = []
    for rucksack in data:
        compartment_1, compartment_2 = rucksack
        common_item: str = _common_item(compartment_1, compartment_2)
        item_priority: int = _priority(common_item)
        result.append(item_priority)

    return result


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input()
    data: list[tuple] = _parse(puzzle_input)

    print(f"Answer for part 1: {sum(_common_items_priorities(data))}")

    # print(f"Answer for part 2: {None}")


if __name__ == "__main__":
    main()
