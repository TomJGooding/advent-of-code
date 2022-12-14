import pytest
from solutions import CPULog, _interesting_signal_strengths, _load_puzzle_input, _parse


@pytest.fixture
def example_data_01():
    example_input = _load_puzzle_input(filename="example_01.txt")
    return _parse(example_input)


@pytest.fixture
def example_data_02():
    example_input = _load_puzzle_input(filename="example_02.txt")
    return _parse(example_input)


def test_parse_simple_example(example_data_01):
    cpu = example_data_01
    assert cpu.cycle_counter == 5
    assert cpu.register.value == -1
    assert cpu.log == [
        CPULog(cycle_number=1, register_value=1, processor_active=False),
        CPULog(cycle_number=2, register_value=1, processor_active=True),
        CPULog(cycle_number=3, register_value=1, processor_active=True),
        CPULog(cycle_number=4, register_value=4, processor_active=True),
        CPULog(cycle_number=5, register_value=4, processor_active=True),
    ]


def test_interesting_signal_strengths(example_data_02):
    cpu_log = example_data_02.log
    assert _interesting_signal_strengths(cpu_log) == [
        420,
        1140,
        1800,
        2940,
        2880,
        3960,
    ]
