import pytest
from solutions import (
    DirectionType,
    Knot,
    KnotType,
    Motion,
    _load_puzzle_input,
    _move_tail_knot,
    _parse,
    _run_knot_motions,
    is_touching,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


@pytest.fixture
def head_knot():
    return Knot(
        x=0,
        y=0,
        type=KnotType.HEAD,
        positions_visited=[(0, 0)],
    )


@pytest.fixture
def tail_knot():
    return Knot(
        x=0,
        y=0,
        type=KnotType.TAIL,
        positions_visited=[(0, 0)],
    )


def test_parse(example_data):
    assert example_data == [
        Motion(DirectionType.RIGHT, 4),
        Motion(DirectionType.UP, 4),
        Motion(DirectionType.LEFT, 3),
        Motion(DirectionType.DOWN, 1),
        Motion(DirectionType.RIGHT, 4),
        Motion(DirectionType.DOWN, 1),
        Motion(DirectionType.LEFT, 5),
        Motion(DirectionType.RIGHT, 2),
    ]


def test_run_test_motions_with_head_knot_final_position(
    example_data, head_knot, tail_knot
):
    series_motions = example_data
    head_knot = head_knot
    tail_knot = tail_knot
    _run_knot_motions(series_motions, head_knot, tail_knot)
    assert head_knot.positions_visited[-1] == (2, 2)


def testis_touching_when_true(head_knot):
    head_knot = head_knot

    tail_touching_up = Knot(
        x=0,
        y=1,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_down = Knot(
        x=0,
        y=-1,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_left = Knot(
        x=-1,
        y=0,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_right = Knot(
        x=1,
        y=0,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_diagonal = Knot(
        x=1,
        y=-1,
        type=KnotType.TAIL,
        positions_visited=[],
    )

    assert is_touching(head_knot, tail_touching_up)
    assert is_touching(head_knot, tail_touching_down)
    assert is_touching(head_knot, tail_touching_left)
    assert is_touching(head_knot, tail_touching_right)
    assert is_touching(head_knot, tail_touching_diagonal)


def testis_touching_when_false(head_knot):
    head_knot = head_knot

    tail_touching_up = Knot(
        x=0,
        y=2,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_down = Knot(
        x=0,
        y=-2,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_left = Knot(
        x=-2,
        y=0,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_right = Knot(
        x=2,
        y=0,
        type=KnotType.TAIL,
        positions_visited=[],
    )
    tail_touching_diagonal = Knot(
        x=2,
        y=-1,
        type=KnotType.TAIL,
        positions_visited=[],
    )

    assert not is_touching(head_knot, tail_touching_up)
    assert not is_touching(head_knot, tail_touching_down)
    assert not is_touching(head_knot, tail_touching_left)
    assert not is_touching(head_knot, tail_touching_right)
    assert not is_touching(head_knot, tail_touching_diagonal)


def test_run_test_motions_with_tail_knot_final_position(
    example_data, head_knot, tail_knot
):
    series_motions = example_data
    head_knot = head_knot
    tail_knot = tail_knot
    _run_knot_motions(series_motions, head_knot, tail_knot)
    assert tail_knot.positions_visited[-1] == (1, 2)


def test_move_tail_knot_straight_up(head_knot):
    head_knot = head_knot
    tail_knot = Knot(x=0, y=-2, type=KnotType.TAIL, positions_visited=[])
    motion = Motion(DirectionType.UP, steps=1)
    _move_tail_knot(head_knot, tail_knot, motion)
    assert tail_knot.x == 0
    assert tail_knot.y == -1


def test_move_tail_knot_straight_right(head_knot):
    head_knot = head_knot
    tail_knot = Knot(x=-2, y=0, type=KnotType.TAIL, positions_visited=[])
    motion = Motion(DirectionType.RIGHT, steps=1)
    _move_tail_knot(head_knot, tail_knot, motion)
    assert tail_knot.x == -1
    assert tail_knot.y == 0


def test_move_tail_knot_diagonally_up_right(head_knot):
    head_knot = head_knot
    tail_knot = Knot(x=-1, y=-2, type=KnotType.TAIL, positions_visited=[])
    motion = Motion(DirectionType.UP, steps=1)
    _move_tail_knot(head_knot, tail_knot, motion)
    assert tail_knot.x == 0
    assert tail_knot.y == -1
