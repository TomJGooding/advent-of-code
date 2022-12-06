from enum import Enum
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 2: Rock Paper Scissors ---"
PUZZLE_DIR = Path(__file__).parent


class PlayerHand(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class OpponentHand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class HandScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RoundScore(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


PLAYER_VICTORIES = [
    (OpponentHand.SCISSORS, PlayerHand.ROCK),
    (OpponentHand.ROCK, PlayerHand.PAPER),
    (OpponentHand.PAPER, PlayerHand.SCISSORS),
]


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str) -> list[tuple]:
    data: list[tuple] = []
    for line in puzzle_input.splitlines():
        round: list[str] = line.split()
        opponent_hand = OpponentHand(round[0])
        player_hand = PlayerHand(round[1])
        data.append((opponent_hand, player_hand))

    return data


def _total_player_score(data: list[tuple]) -> int:
    player_score: int = 0
    for round in data:
        opponent_hand, player_hand = round
        player_score += HandScore[player_hand.name].value

        if opponent_hand.name == player_hand.name:
            player_score += RoundScore.DRAW.value
        elif round in PLAYER_VICTORIES:
            player_score += RoundScore.WIN.value
        else:
            player_score += RoundScore.LOSS.value

    return player_score


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input()
    data: list[tuple] = _parse(puzzle_input)
    print(f"Answer for part 1: {_total_player_score(data)}")

    # print(f"Answer for part 2: {None}")


if __name__ == "__main__":
    main()
