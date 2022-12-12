from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 9: Rope Bridge ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


class DirectionType(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Motion:
    direction: DirectionType
    steps: int


class KnotType(Enum):
    HEAD = "H"
    TAIL = "T"


@dataclass
class Knot:
    x: int
    y: int
    type: KnotType
    positions_visited: list[tuple]

    def move_to(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self.positions_visited.append((x, y))


def _parse(puzzle_input: str) -> list[Motion]:
    data: list[Motion] = []
    for line in puzzle_input.splitlines():
        direction, steps = line.split()
        direction_type = DirectionType(direction)
        num_steps = int(steps)
        data.append(Motion(direction_type, num_steps))

    return data


def _run_knot_motions(
    series_motions: list[Motion], head_knot: Knot, tail_knot: Knot
) -> tuple[Knot, Knot]:
    for motion in series_motions:
        if motion.direction == DirectionType.UP:
            for _ in range(motion.steps):
                head_knot.move_to(head_knot.x, head_knot.y + 1)
                if not is_touching(head_knot, tail_knot):
                    _move_tail_knot(head_knot, tail_knot, motion)

        elif motion.direction == DirectionType.DOWN:
            for _ in range(motion.steps):
                head_knot.move_to(head_knot.x, head_knot.y - 1)
                if not is_touching(head_knot, tail_knot):
                    _move_tail_knot(head_knot, tail_knot, motion)

        elif motion.direction == DirectionType.LEFT:
            for _ in range(motion.steps):
                head_knot.move_to(head_knot.x - 1, head_knot.y)
                if not is_touching(head_knot, tail_knot):
                    _move_tail_knot(head_knot, tail_knot, motion)

        elif motion.direction == DirectionType.RIGHT:
            for _ in range(motion.steps):
                head_knot.move_to(head_knot.x + 1, head_knot.y)
                if not is_touching(head_knot, tail_knot):
                    _move_tail_knot(head_knot, tail_knot, motion)

    return head_knot, tail_knot


def is_touching(head_knot: Knot, tail_knot: Knot) -> bool:
    return head_knot.x - tail_knot.x in range(
        -1, 2
    ) and head_knot.y - tail_knot.y in range(-1, 2)


def _move_tail_knot(head_knot: Knot, tail_knot: Knot, motion: Motion) -> None:
    if motion.direction == DirectionType.UP:
        x_diff: int = head_knot.x - tail_knot.x
        tail_knot.move_to(tail_knot.x + x_diff, tail_knot.y + 1)
    elif motion.direction == DirectionType.DOWN:
        x_diff: int = head_knot.x - tail_knot.x
        tail_knot.move_to(tail_knot.x + x_diff, tail_knot.y - 1)
    elif motion.direction == DirectionType.LEFT:
        y_diff: int = head_knot.y - tail_knot.y
        tail_knot.move_to(tail_knot.x - 1, tail_knot.y + y_diff)
    elif motion.direction == DirectionType.RIGHT:
        y_diff: int = head_knot.y - tail_knot.y
        tail_knot.move_to(tail_knot.x + 1, tail_knot.y + y_diff)


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    series_motions: list[Motion] = _parse(puzzle_input)
    head_knot = Knot(x=0, y=0, type=KnotType.HEAD, positions_visited=[(0, 0)])
    tail_knot = Knot(x=0, y=0, type=KnotType.TAIL, positions_visited=[(0, 0)])

    _run_knot_motions(series_motions, head_knot, tail_knot)

    tail_knot_unique_positions = set(tail_knot.positions_visited)
    print(f"Answer for part 1: {len(tail_knot_unique_positions)}")


if __name__ == "__main__":
    main()
