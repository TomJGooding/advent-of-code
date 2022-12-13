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
    NONE = "N"


@dataclass
class Motion:
    direction: DirectionType
    steps: int


@dataclass
class Knot:
    x: int
    y: int
    positions_visited: list[tuple]
    last_direction: DirectionType = DirectionType.NONE

    def move_to(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self.positions_visited.append((x, y))


class Rope:
    def __init__(self) -> None:
        self.knots: list[Knot] = []


def _parse(puzzle_input: str) -> list[Motion]:
    data: list[Motion] = []
    for line in puzzle_input.splitlines():
        direction, steps = line.split()
        direction_type = DirectionType(direction)
        num_steps = int(steps)
        data.append(Motion(direction_type, num_steps))

    return data


def _run_motions(series_motions: list[Motion], rope: Rope) -> Rope:
    for motion in series_motions:
        for _ in range(motion.steps):
            for idx, knot in enumerate(rope.knots):
                if idx == 0:
                    _move_head_knot(knot, motion)
                    continue

                if not is_touching(
                    knot_ahead=rope.knots[idx - 1],
                    curr_knot=knot,
                ):
                    _move_curr_knot(
                        knot_ahead=rope.knots[idx - 1],
                        curr_knot=knot,
                    )

    return rope


def _move_head_knot(knot: Knot, motion: Motion) -> None:
    if motion.direction == DirectionType.UP:
        knot.move_to(knot.x, knot.y + 1)
        knot.last_direction = DirectionType.UP

    elif motion.direction == DirectionType.DOWN:
        knot.move_to(knot.x, knot.y - 1)
        knot.last_direction = DirectionType.DOWN

    elif motion.direction == DirectionType.LEFT:
        knot.move_to(knot.x - 1, knot.y)
        knot.last_direction = DirectionType.LEFT

    elif motion.direction == DirectionType.RIGHT:
        knot.move_to(knot.x + 1, knot.y)
        knot.last_direction = DirectionType.RIGHT


def is_touching(knot_ahead: Knot, curr_knot: Knot) -> bool:
    return knot_ahead.x - curr_knot.x in range(
        -1, 2
    ) and knot_ahead.y - curr_knot.y in range(-1, 2)


def _move_curr_knot(knot_ahead: Knot, curr_knot: Knot) -> None:
    x_diff: int = knot_ahead.x - curr_knot.x
    y_diff: int = knot_ahead.y - curr_knot.y

    if knot_ahead.last_direction == DirectionType.UP:
        curr_knot.move_to(curr_knot.x + x_diff, curr_knot.y + 1)

    elif knot_ahead.last_direction == DirectionType.DOWN:
        curr_knot.move_to(curr_knot.x + x_diff, curr_knot.y - 1)

    elif knot_ahead.last_direction == DirectionType.LEFT:
        curr_knot.move_to(curr_knot.x - 1, curr_knot.y + y_diff)

    elif knot_ahead.last_direction == DirectionType.RIGHT:
        curr_knot.move_to(curr_knot.x + 1, curr_knot.y + y_diff)


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    series_motions: list[Motion] = _parse(puzzle_input)

    short_rope = Rope()
    for _ in range(2):
        short_rope.knots.append(Knot(x=0, y=0, positions_visited=[(0, 0)]))
    _run_motions(series_motions, short_rope)
    short_rope_tail = short_rope.knots[-1]
    print(f"Answer for part 1: {len(set(short_rope_tail.positions_visited))}")


if __name__ == "__main__":
    main()
