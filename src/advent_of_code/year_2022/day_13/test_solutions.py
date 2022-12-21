import pytest
from solutions import (
    _compare,
    _find_indexes_of_packet_pairs_in_correct_order,
    _load_puzzle_input,
    _parse,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_parse(example_data):
    assert len(example_data) == 8
    assert example_data == [
        [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
        [[[1], [2, 3, 4]], [[1], 4]],
        [[9], [[8, 7, 6]]],
        [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[], [3]],
        [[[[]]], [[]]],
        [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]],
    ]


def test_compare_when_both_integers():
    smaller_left = 3
    larger_left = 7
    right = 5
    assert _compare(smaller_left, right) == -2
    assert _compare(larger_left, right) == 2


def test_compare_when_both_lists():
    left = [1, 1, 3, 1, 1]
    right = [1, 1, 5, 1, 1]
    assert _compare(left, right) == -2


def test_compare_when_mixed_types():
    left = 9
    right = [8, 7, 6]
    assert _compare(left, right) == 1


def test_find_indexes_of_packet_pairs_in_correct_order(example_data):
    assert _find_indexes_of_packet_pairs_in_correct_order(
        packet_pairs=example_data
    ) == [1, 2, 4, 6]
