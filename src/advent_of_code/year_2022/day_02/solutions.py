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


class RoundOutcome(Enum):
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"


PLAYER_WINS = [
    (OpponentHand.SCISSORS, PlayerHand.ROCK),
    (OpponentHand.ROCK, PlayerHand.PAPER),
    (OpponentHand.PAPER, PlayerHand.SCISSORS),
]

PLAYER_LOSSES = [
    (OpponentHand.ROCK, PlayerHand.SCISSORS),
    (OpponentHand.PAPER, PlayerHand.ROCK),
    (OpponentHand.SCISSORS, PlayerHand.PAPER),
]


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str, puzzle_part: int) -> list[tuple]:
    data: list[tuple] = []
    for line in puzzle_input.splitlines():
        round: list[str] = line.split()
        opponent_hand = OpponentHand(round[0])

        if puzzle_part == 1:
            player_hand = PlayerHand(round[1])
            data.append((opponent_hand, player_hand))

        elif puzzle_part == 2:
            desired_outcome = RoundOutcome(round[1])
            if desired_outcome == RoundOutcome.DRAW:
                player_hand = PlayerHand[opponent_hand.name]
            elif desired_outcome == RoundOutcome.WIN:
                player_wins: dict = {key: val for key, val in PLAYER_WINS}
                player_hand: PlayerHand = player_wins[opponent_hand]
            else:
                player_losses: dict = {key: val for key, val in PLAYER_LOSSES}
                player_hand: PlayerHand = player_losses[opponent_hand]

            data.append((opponent_hand, player_hand))

    return data


def _total_player_score(data: list[tuple]) -> int:
    player_score: int = 0
    for round in data:
        opponent_hand, player_hand = round
        player_score += HandScore[player_hand.name].value

        if opponent_hand.name == player_hand.name:
            player_score += RoundScore.DRAW.value
        elif round in PLAYER_WINS:
            player_score += RoundScore.WIN.value
        else:
            player_score += RoundScore.LOSS.value

    return player_score


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input()

    data_part_1: list[tuple] = _parse(puzzle_input, puzzle_part=1)
    print(f"Answer for part 1: {_total_player_score(data_part_1)}")

    data_part_2: list[tuple] = _parse(puzzle_input, puzzle_part=2)
    print(f"Answer for part 2: {_total_player_score(data_part_2)}")


if __name__ == "__main__":
    main()
