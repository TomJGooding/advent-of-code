import pytest
from solutions import _common_item, _common_items_priorities, _load_puzzle_input, _parse


@pytest.fixture
def example_data_part_1():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input, puzzle_part=1)


@pytest.fixture
def example_data_part_2():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input, puzzle_part=2)


def test_parse_part_1(example_data_part_1):
    expected_sample = [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
    ]
    assert example_data_part_1[:3] == expected_sample


def test_parse_part_2(example_data_part_2):
    assert example_data_part_2 == [
        (
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ),
        (
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ),
    ]


def test_common_item():
    rucksack = ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    assert _common_item(rucksack) == "p"


def test_common_items_priorities(example_data_part_1):
    assert _common_items_priorities(example_data_part_1) == [
        16,
        38,
        42,
        22,
        20,
        19,
    ]
