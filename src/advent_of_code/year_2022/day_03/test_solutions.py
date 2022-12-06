import pytest
from solutions import _common_item, _common_items_priorities, _load_puzzle_input, _parse


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_parse(example_data):
    expected_sample = [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
    ]
    assert example_data[:3] == expected_sample


def test_common_item():
    rucksack = ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    compartment_1, compartment_2 = rucksack
    assert _common_item(compartment_1, compartment_2) == "p"


def test_common_items_priorities(example_data):
    assert _common_items_priorities(example_data) == [
        16,
        38,
        42,
        22,
        20,
        19,
    ]
