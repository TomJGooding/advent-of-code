import pytest
from solutions import (
    MESSAGE_MARKER,
    PACKET_MARKER,
    _find_first_marker_idx,
    _load_puzzle_input,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return [line for line in example_input.splitlines()]


def test_start_of_packet(example_data):
    expected = [7, 5, 6, 10, 11]
    result = [_find_first_marker_idx(PACKET_MARKER, buffer) for buffer in example_data]
    assert result == expected


def test_start_of_message(example_data):
    expected = [19, 23, 23, 29, 26]
    result = [_find_first_marker_idx(MESSAGE_MARKER, buffer) for buffer in example_data]
    assert result == expected
