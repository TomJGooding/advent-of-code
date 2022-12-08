import pytest
from solutions import (
    _crate_stacks,
    _load_puzzle_input,
    _parse,
    _parse_crates_rows,
    _parse_rearrangement_steps,
    _rearrange_stacks,
    _top_crates_message,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


@pytest.fixture
def example_crates_rows():
    example_input = _load_puzzle_input(filename="example.txt")
    crates_input, _ = example_input.split("\n\n")
    return _parse_crates_rows(crates_input)


def test_parse_crates_rows(example_crates_rows):
    assert example_crates_rows == [
        ["", "[D]", ""],
        ["[N]", "[C]", ""],
        ["[Z]", "[M]", "[P]"],
    ]


def test_crate_stacks(example_crates_rows):
    crate_stacks = _crate_stacks(example_crates_rows)
    assert crate_stacks == [
        ["[Z]", "[N]"],
        ["[M]", "[C]", "[D]"],
        ["[P]"],
    ]


def test_parse_rearrangement_steps():
    example_input = _load_puzzle_input(filename="example.txt")
    _, rearrangement_input = example_input.split("\n\n")
    assert _parse_rearrangement_steps(rearrangement_input) == [
        {"num_crates": 1, "from_stack": 2, "to_stack": 1},
        {"num_crates": 3, "from_stack": 1, "to_stack": 3},
        {"num_crates": 2, "from_stack": 2, "to_stack": 1},
        {"num_crates": 1, "from_stack": 1, "to_stack": 2},
    ]


def test_rearrange_crate_stacks_part1(example_data):
    crate_stacks, rearrangement_steps = example_data
    assert _rearrange_stacks(
        crate_stacks, rearrangement_steps, crane_model="CrateMover 9000"
    ) == [
        ["[C]"],
        ["[M]"],
        ["[P]", "[D]", "[N]", "[Z]"],
    ]


def test_top_crates_message():
    stacks = [
        ["[C]"],
        ["[M]"],
        ["[P]", "[D]", "[N]", "[Z]"],
    ]
    assert _top_crates_message(stacks) == "CMZ"


def test_rearrange_crate_stacks_part2(example_data):
    crate_stacks, rearrangement_steps = example_data
    assert _rearrange_stacks(
        crate_stacks, rearrangement_steps, crane_model="CrateMover 9001"
    ) == [
        ["[M]"],
        ["[C]"],
        ["[P]", "[Z]", "[N]", "[D]"],
    ]
