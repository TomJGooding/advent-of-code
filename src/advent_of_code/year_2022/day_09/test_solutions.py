import pytest
from solutions import (
    DirectionType,
    Knot,
    Motion,
    Rope,
    _load_puzzle_input,
    _move_curr_knot,
    _parse,
    _run_motions,
    is_touching,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


@pytest.fixture
def example_data_2():
    example_input = _load_puzzle_input(filename="example_2.txt")
    return _parse(example_input)


@pytest.fixture
def short_rope():
    short_rope = Rope()
    for _ in range(2):
        short_rope.knots.append(Knot(x=0, y=0, positions_visited=[(0, 0)]))
    return short_rope


@pytest.fixture
def long_rope():
    long_rope = Rope()
    for _ in range(10):
        long_rope.knots.append(Knot(x=0, y=0, positions_visited=[(0, 0)]))
    return long_rope


@pytest.fixture
def head_knot():
    return Knot(x=0, y=0, positions_visited=[(0, 0)])


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
    example_data,
    short_rope,
):
    short_rope = short_rope
    series_motions = example_data
    _run_motions(series_motions, short_rope)
    head_knot = short_rope.knots[0]
    assert head_knot.positions_visited[-1] == (2, 2)


def test_is_touching_when_true(head_knot):
    head_knot = head_knot

    tail_touching_up = Knot(x=0, y=1, positions_visited=[])
    tail_touching_down = Knot(x=0, y=-1, positions_visited=[])
    tail_touching_left = Knot(x=-1, y=0, positions_visited=[])
    tail_touching_right = Knot(x=1, y=0, positions_visited=[])
    tail_touching_diagonal = Knot(x=1, y=-1, positions_visited=[])

    assert is_touching(head_knot, tail_touching_up)
    assert is_touching(head_knot, tail_touching_down)
    assert is_touching(head_knot, tail_touching_left)
    assert is_touching(head_knot, tail_touching_right)
    assert is_touching(head_knot, tail_touching_diagonal)


def test_is_touching_when_false(head_knot):
    head_knot = head_knot

    tail_touching_up = Knot(x=0, y=2, positions_visited=[])
    tail_touching_down = Knot(x=0, y=-2, positions_visited=[])
    tail_touching_left = Knot(x=-2, y=0, positions_visited=[])
    tail_touching_right = Knot(x=2, y=0, positions_visited=[])
    tail_touching_diagonal = Knot(x=2, y=-1, positions_visited=[])

    assert not is_touching(head_knot, tail_touching_up)
    assert not is_touching(head_knot, tail_touching_down)
    assert not is_touching(head_knot, tail_touching_left)
    assert not is_touching(head_knot, tail_touching_right)
    assert not is_touching(head_knot, tail_touching_diagonal)


def test_run_test_motions_with_tail_knot_final_position(
    example_data,
    short_rope,
):
    series_motions = example_data
    short_rope = short_rope
    _run_motions(series_motions, short_rope)
    head_knot = short_rope.knots[0]
    tail_knot = short_rope.knots[-1]
    assert tail_knot.positions_visited != head_knot.positions_visited
    assert tail_knot.positions_visited[-1] == (1, 2)


def test_move_curr_knot_straight_up(head_knot):
    head_knot.last_direction = DirectionType.UP
    tail_knot = Knot(x=0, y=-2, positions_visited=[])
    _move_curr_knot(head_knot, tail_knot)
    assert tail_knot.x == 0
    assert tail_knot.y == -1


def test_move_curr_knot_straight_right(head_knot):
    head_knot.last_direction = DirectionType.RIGHT
    tail_knot = Knot(x=-2, y=0, positions_visited=[])
    _move_curr_knot(head_knot, tail_knot)
    assert tail_knot.x == -1
    assert tail_knot.y == 0


def test_move_curr_knot_diagonally_up_right(head_knot):
    head_knot.last_direction = DirectionType.UP
    tail_knot = Knot(x=-1, y=-2, positions_visited=[])
    _move_curr_knot(head_knot, tail_knot)
    assert tail_knot.x == 0
    assert tail_knot.y == -1
