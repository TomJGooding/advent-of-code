import pytest
from solutions import (
    Item,
    Monkey,
    _calculate_monkey_business,
    _load_puzzle_input,
    _parse,
    _play_monkey_in_the_middle,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_parse(example_data):
    assert example_data == [
        Monkey(
            items=[Item(79), Item(98)],
            inspect_operation="* 19",
            divisible_test=23,
            test_true_throw_to_monkey=2,
            test_false_throw_to_monkey=3,
        ),
        Monkey(
            items=[Item(54), Item(65), Item(75), Item(74)],
            inspect_operation="+ 6",
            divisible_test=19,
            test_true_throw_to_monkey=2,
            test_false_throw_to_monkey=0,
        ),
        Monkey(
            items=[Item(79), Item(60), Item(97)],
            inspect_operation="* old",
            divisible_test=13,
            test_true_throw_to_monkey=1,
            test_false_throw_to_monkey=3,
        ),
        Monkey(
            items=[Item(74)],
            inspect_operation="+ 3",
            divisible_test=17,
            test_true_throw_to_monkey=0,
            test_false_throw_to_monkey=1,
        ),
    ]


def test_play_monkey_in_the_middle_with_single_round(example_data):
    actual = _play_monkey_in_the_middle(
        monkeys=example_data,
        number_rounds=1,
    )
    expected = [
        Monkey(
            items=[Item(20), Item(23), Item(27), Item(26)],
            inspect_operation="* 19",
            divisible_test=23,
            test_true_throw_to_monkey=2,
            test_false_throw_to_monkey=3,
            count_inspections=2,
        ),
        Monkey(
            items=[
                Item(2080),
                Item(25),
                Item(167),
                Item(207),
                Item(401),
                Item(1046),
            ],
            inspect_operation="+ 6",
            divisible_test=19,
            test_true_throw_to_monkey=2,
            test_false_throw_to_monkey=0,
            count_inspections=4,
        ),
        Monkey(
            items=[],
            inspect_operation="* old",
            divisible_test=13,
            test_true_throw_to_monkey=1,
            test_false_throw_to_monkey=3,
            count_inspections=3,
        ),
        Monkey(
            items=[],
            inspect_operation="+ 3",
            divisible_test=17,
            test_true_throw_to_monkey=0,
            test_false_throw_to_monkey=1,
            count_inspections=5,
        ),
    ]
    assert actual == expected


def test_play_monkey_in_the_middle_with_twenty_rounds(example_data):
    new_monkeys = _play_monkey_in_the_middle(monkeys=example_data)
    actual = [monkey.count_inspections for monkey in new_monkeys]
    expected = [101, 95, 7, 105]
    assert actual == expected
    assert _calculate_monkey_business(new_monkeys) == 10605
