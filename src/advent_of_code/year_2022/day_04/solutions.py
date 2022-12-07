from pathlib import Path
from typing import Generator, Optional

PUZZLE_TITLE: str = "--- Day 4: Camp Cleanup ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str) -> list[list[range]]:
    data: list[list[range]] = []
    for line in puzzle_input.splitlines():
        pair_assignments: list[str] = line.split(",")

        section_ranges: list[range] = []
        for assignment in pair_assignments:
            start_section, end_section = [
                int(section) for section in assignment.split("-")
            ]
            section_range: range = range(start_section, end_section + 1)
            section_ranges.append(section_range)

        data.append(section_ranges)

    return data


def _range_overlapping(ranges: list[range]) -> Generator:
    ranges_copy = ranges.copy()
    shortest_range: range = min(ranges_copy, key=len)
    ranges_copy.remove(shortest_range)

    for i in shortest_range:
        if all(i in range_ for range_ in ranges_copy):
            yield i


def _total_fully_overlapping_ranges(data: list[list[range]]) -> int:
    count: int = 0
    for ranges in data:
        shortest_range: range = min(ranges, key=len)
        range_overlapping: list[int] = list(_range_overlapping(ranges))
        if list(shortest_range) == range_overlapping:
            count += 1

    return count


def _total_overlapping_ranges(data: list[list[range]]) -> int:
    count: int = 0
    for ranges in data:
        if list(_range_overlapping(ranges)):
            count += 1

    return count


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    data = _parse(puzzle_input)
    print(f"Answer for part 1: {_total_fully_overlapping_ranges(data)}")
    print(f"Answer for part 2: {_total_overlapping_ranges(data)}")


if __name__ == "__main__":
    main()
