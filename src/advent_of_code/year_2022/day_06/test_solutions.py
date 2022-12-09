import pytest
from solutions import _load_puzzle_input, _start_of_packet_idx


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return [line for line in example_input.splitlines()]


def test_start_of_packet_idx(example_data):
    expected = [7, 5, 6, 10, 11]
    result = [_start_of_packet_idx(buffer) for buffer in example_data]
    assert result == expected
