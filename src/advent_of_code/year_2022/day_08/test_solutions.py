import pytest
from solutions import (
    _load_puzzle_input,
    _parse,
    _total_visible_trees,
    _trees_above,
    _trees_below,
    _trees_left,
    _trees_right,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_trees_right(example_data):
    row_idx, col_idx = 2, 2
    assert _trees_right(example_data, row_idx, col_idx) == [3, 2]


def test_trees_left(example_data):
    row_idx, col_idx = 2, 2
    assert _trees_left(example_data, row_idx, col_idx) == [6, 5]


def test_trees_above(example_data):
    row_idx, col_idx = 2, 2
    assert _trees_above(example_data, row_idx, col_idx) == [3, 5]


def test_trees_below(example_data):
    row_idx, col_idx = 2, 2
    assert _trees_below(example_data, row_idx, col_idx) == [5, 3]


def test_total_visible_trees(example_data):
    assert _total_visible_trees(example_data) == 21
