import pytest
from solutions import (
    _load_puzzle_input,
    _parse,
    _range_overlapping,
    _total_fully_overlapping_ranges,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_parse(example_data):
    assert example_data == [
        [range(2, 5), range(6, 9)],
        [range(2, 4), range(4, 6)],
        [range(5, 8), range(7, 10)],
        [range(2, 9), range(3, 8)],
        [range(6, 7), range(4, 7)],
        [range(2, 7), range(4, 9)],
    ]


def test_range_overlapping():
    ranges = [range(2, 9), range(3, 8)]
    range_overlapping = list(_range_overlapping(ranges))
    assert range_overlapping == [3, 4, 5, 6, 7]


def test_range_intersection_when_none():
    ranges = [range(2, 5), range(6, 9)]
    range_interection = list(_range_overlapping(ranges))
    assert not range_interection


def test_total_fully_overlapping_ranges(example_data):
    assert _total_fully_overlapping_ranges(example_data) == 2
