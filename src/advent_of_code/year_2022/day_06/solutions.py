from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 6: Tuning Trouble ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _start_of_packet_idx(datastream_buffer: str) -> int:
    result: int = 0
    for idx, _ in enumerate(datastream_buffer, start=4):
        prev_four = datastream_buffer[idx - 4 : idx]
        if len(set(prev_four)) == 4:
            result = idx
            break

    return result


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    datastream_buffer: str = puzzle_input
    print(f"Answer for part 1: {_start_of_packet_idx(datastream_buffer)}")


if __name__ == "__main__":
    main()
