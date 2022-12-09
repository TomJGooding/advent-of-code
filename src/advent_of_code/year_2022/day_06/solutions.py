from dataclasses import dataclass
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 6: Tuning Trouble ---"
PUZZLE_DIR = Path(__file__).parent


@dataclass
class Marker:
    after_unique: int


PACKET_MARKER = Marker(after_unique=4)
MESSAGE_MARKER = Marker(after_unique=14)


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _find_first_marker_idx(marker: Marker, datastream_buffer: str) -> int:
    result: int = 0
    for idx, _ in enumerate(datastream_buffer, start=marker.after_unique):
        prev_chunk = datastream_buffer[idx - marker.after_unique : idx]
        if len(set(prev_chunk)) == marker.after_unique:
            result = idx
            break

    return result


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    buffer: str = puzzle_input
    print(f"Answer for part 1: {_find_first_marker_idx(MESSAGE_MARKER, buffer,)}")


if __name__ == "__main__":
    main()
