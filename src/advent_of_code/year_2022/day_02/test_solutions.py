import pytest
from solutions import (
    HandScore,
    OpponentHand,
    PlayerHand,
    _load_puzzle_input,
    _parse,
    _total_player_score,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_hands_comparison():
    opponent_turn = OpponentHand("A")
    player_turn = PlayerHand("X")
    assert player_turn.name == opponent_turn.name
    assert (opponent_turn, player_turn) == (OpponentHand.ROCK, PlayerHand.ROCK)


def test_parse(example_data):
    assert example_data == [
        (OpponentHand.ROCK, PlayerHand.PAPER),
        (OpponentHand.PAPER, PlayerHand.ROCK),
        (OpponentHand.SCISSORS, PlayerHand.SCISSORS),
    ]


def test_hand_score():
    rock = PlayerHand.ROCK.name
    paper = PlayerHand.PAPER.name
    scissors = PlayerHand.SCISSORS.name
    assert HandScore[rock].value == 1
    assert HandScore[paper].value == 2
    assert HandScore[scissors].value == 3


def test_total_player_score(example_data):
    total_player_score = _total_player_score(example_data)
    assert total_player_score == 15
