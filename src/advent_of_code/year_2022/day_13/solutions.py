import json
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 13: Distress Signal ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str) -> list[list]:
    packet_pairs: list[list] = []
    for pair in puzzle_input.split("\n\n"):
        packet_pairs.append([json.loads(e) for e in pair.splitlines()])

    return packet_pairs


def _find_indexes_of_packet_pairs_in_correct_order(
    packet_pairs: list[list],
) -> list[int]:
    result: list[int] = []
    for idx, (left, right) in enumerate(packet_pairs, start=1):
        if _compare(left, right) > 0:
            continue

        result.append(idx)

    return result


def _compare(left: list | int, right: list | int) -> int:
    left_is_int: bool = isinstance(left, int)
    right_is_int: bool = isinstance(right, int)

    if left_is_int and right_is_int:
        return left - right

    elif left_is_int != right_is_int:
        if left_is_int:
            return _compare([left], right)
        elif right_is_int:
            return _compare(left, [right])

    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            result = _compare(a, b)
            if result != 0:
                return result

        return len(left) - len(right)

    raise TypeError


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    packet_pairs = _parse(puzzle_input)

    print(
        "Answer for part 1:",
        sum(_find_indexes_of_packet_pairs_in_correct_order(packet_pairs)),
    )


if __name__ == "__main__":
    main()
