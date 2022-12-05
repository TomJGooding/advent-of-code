import pytest
from solutions import highest_total_calories, load_puzzle_input, parse


@pytest.fixture
def example_data():
    example_input = load_puzzle_input(filename="example.txt")
    return parse(example_input)


def test_parse(example_data):
    assert example_data == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_highest_total_calories(example_data):
    assert highest_total_calories(example_data) == 24000
