import pytest
from solutions import (
    _highest_total_calories,
    _load_puzzle_input,
    _parse,
    _top_3_total_calories,
    _total_calories_per_elf,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


@pytest.fixture
def example_total_calories():
    return [6000, 4000, 11000, 24000, 10000]


def test_parse(example_data):
    assert example_data == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_total_calories_per_elf(example_data):
    assert _total_calories_per_elf(example_data) == [
        6000,
        4000,
        11000,
        24000,
        10000,
    ]


def test_highest_total_calories(example_total_calories):
    assert _highest_total_calories(example_total_calories) == 24000


def test_top_3_total_calories(example_total_calories):
    assert _top_3_total_calories(example_total_calories) == [
        10000,
        11000,
        24000,
    ]
