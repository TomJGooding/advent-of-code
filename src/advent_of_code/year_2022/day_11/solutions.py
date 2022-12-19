import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 11: Monkey in the Middle ---"
PUZZLE_DIR = Path(__file__).parent

NUMBER_ROUNDS: int = 20


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


@dataclass
class Item:
    worry_level: int


@dataclass
class Throw:
    item: Item
    to_monkey_id: int


@dataclass
class Monkey:
    items: list[Item]
    inspect_operation: str
    divisible_test: int
    test_true_throw_to_monkey: int
    test_false_throw_to_monkey: int
    count_inspections: int = 0

    def inspect_item(self) -> None:
        worry_level: int = self.items[0].worry_level
        operator, input = self.inspect_operation.split()
        input_num: int = int(input) if input != "old" else worry_level
        if operator == "+":
            worry_level += input_num
        elif operator == "*":
            worry_level *= input_num

        self.count_inspections += 1
        self.items[0].worry_level = worry_level // 3

    def throw_item(self) -> Throw:
        if self.test_item() is True:
            throw = Throw(
                item=self.items.pop(0),
                to_monkey_id=self.test_true_throw_to_monkey,
            )
        else:
            throw = Throw(
                item=self.items.pop(0),
                to_monkey_id=self.test_false_throw_to_monkey,
            )
        return throw

    def test_item(self) -> bool:
        return self.items[0].worry_level % self.divisible_test == 0


def _parse(puzzle_input: str) -> list[Monkey]:
    items_pattern = re.compile(r"(?<=Starting items:\s).*")
    operation_pattern = re.compile(r"(?<=Operation: new = old ).*")
    divisible_pattern = re.compile(r"(?<=Test: divisible by )\d+")
    if_true_throw_pattern = re.compile(r"(?<=If true: throw to monkey )\d+")
    if_false_throw_pattern = re.compile(r"(?<=If false: throw to monkey )\d+")

    monkeys: list[Monkey] = []
    for input in puzzle_input.split("\n\n"):
        items_match = items_pattern.search(input)
        operation_match = operation_pattern.search(input)
        divisible_match = divisible_pattern.search(input)
        if_true_throw_match = if_true_throw_pattern.search(input)
        if_false_throw_match = if_false_throw_pattern.search(input)

        if (
            items_match
            and operation_match
            and divisible_match
            and if_true_throw_match
            and if_false_throw_match
        ):
            inspect_operation: str = operation_match.group()
            divisible_test = int(divisible_match.group())
            test_true_throw_to_monkey = int(if_true_throw_match.group())
            test_false_throw_to_monkey = int(if_false_throw_match.group())

            starting_items: list[Item] = []
            for x in items_match.group().split(", "):
                starting_items.append(Item(int(x)))

            monkeys.append(
                Monkey(
                    starting_items,
                    inspect_operation,
                    divisible_test,
                    test_true_throw_to_monkey,
                    test_false_throw_to_monkey,
                )
            )

    return monkeys


def _play_monkey_in_the_middle(
    monkeys: list[Monkey], number_rounds: int = NUMBER_ROUNDS
) -> list[Monkey]:
    new_monkeys = monkeys.copy()
    for _ in range(number_rounds):
        for monkey in new_monkeys:
            while monkey.items:
                monkey.inspect_item()
                throw: Throw = monkey.throw_item()
                new_monkeys[throw.to_monkey_id].items.append(throw.item)

    return new_monkeys


def _sort_monkeys_by_activity(monkeys: list[Monkey]) -> list[Monkey]:
    return sorted(
        [monkey for monkey in monkeys],
        key=_get_count_inspections,
        reverse=True,
    )


def _calculate_monkey_business(monkeys: list[Monkey]) -> int:
    two_most_active: list[Monkey] = _sort_monkeys_by_activity(monkeys)[:2]
    return math.prod([monkey.count_inspections for monkey in two_most_active])


def _get_count_inspections(monkey: Monkey):
    return monkey.count_inspections


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    monkeys = _parse(puzzle_input)

    new_monkeys = _play_monkey_in_the_middle(monkeys)
    print("Answer for part 1: ", _calculate_monkey_business(new_monkeys))


if __name__ == "__main__":
    main()
