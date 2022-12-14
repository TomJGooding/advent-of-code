from dataclasses import dataclass
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 10: Cathode-Ray Tube ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


@dataclass
class Register:
    value: int = 1


@dataclass
class Processor:
    active: bool = False


@dataclass
class CPULog:
    cycle_number: int
    register_value: int
    processor_active: bool


class CPU:
    def __init__(self) -> None:
        self.register = Register()
        self.processor = Processor()
        self.cycle_counter: int = 0
        self.log: list[CPULog] = []

    def execute(self, instruction: str) -> None:
        if instruction == "noop":
            self.processor.active = False
            self.cycle_counter += 1
            self.create_log()
        elif instruction.startswith("addx"):
            for _ in range(2):
                self.processor.active = True
                self.cycle_counter += 1
                self.create_log()
            _, value = instruction.split()
            self.register.value += int(value)

    def create_log(self):
        self.log.append(
            CPULog(
                cycle_number=self.cycle_counter,
                register_value=self.register.value,
                processor_active=self.processor.active,
            )
        )


def _parse(puzzle_input: str) -> CPU:
    cpu = CPU()
    for instruction in puzzle_input.splitlines():
        cpu.execute(instruction)

    return cpu


def _calculate_signal_strength(
    cycle_number: int,
    register_value: int,
) -> int:
    return cycle_number * register_value


def _interesting_signal_strengths(cpu_log: list[CPULog]) -> list[int]:
    result: list[int] = []
    for i in range(20, len(cpu_log), 40):
        for log in cpu_log:
            if log.cycle_number == i:
                result.append(
                    _calculate_signal_strength(
                        log.cycle_number,
                        log.register_value,
                    )
                )

    return result


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    cpu: CPU = _parse(puzzle_input)

    print(
        "Answer for part 1: ",
        sum(_interesting_signal_strengths(cpu.log)),
    )


if __name__ == "__main__":
    main()
