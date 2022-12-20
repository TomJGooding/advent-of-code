from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 12: Hill Climbing Algorithm ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


@dataclass(frozen=True)
class GridSquare:
    coordinates: tuple
    value: str


class HeightMap:
    def __init__(self) -> None:
        self.grid: list[list[GridSquare]] = []

    @property
    def starting_square(self) -> GridSquare:
        return self.find_grid_square_with(value="S")

    @property
    def destination_square(self) -> GridSquare:
        return self.find_grid_square_with(value="E")

    def find_shortest_path(self) -> int:
        visited: set[GridSquare] = set({self.starting_square})
        queue: deque[tuple[GridSquare, int]] = deque([(self.starting_square, 0)])
        while queue:
            current_square, distance = queue.popleft()

            if current_square == self.destination_square:
                return distance

            for neighbour in self.find_neighbours_of(current_square):
                if neighbour not in visited and self.__can_move(
                    current_square,
                    neighbour,
                ):
                    visited.add(neighbour)
                    queue.append((neighbour, distance + 1))

        return -1

    def find_grid_square_with(self, value: str) -> GridSquare:
        for row in self.grid:
            for square in row:
                if square.value == value:
                    return square

        raise ValueError

    def find_neighbours_of(self, grid_square) -> list[GridSquare]:
        x, y = grid_square.coordinates
        result: list[GridSquare] = []
        for i in range(-1, 2, 2):
            if y + i in range(0, len(self.grid)):
                result.append(self.grid[y + i][x])

            if x + i in range(0, len(self.grid[0])):
                result.append(self.grid[y][x + i])

        return result

    @staticmethod
    def __can_move(current_square: GridSquare, neighbour: GridSquare) -> bool:
        if current_square.value == "S":
            current_height: str = "a"
        else:
            current_height = current_square.value
        if neighbour.value == "E":
            neighbour_height: str = "z"
        else:
            neighbour_height = neighbour.value

        height_diff: int = ord(neighbour_height) - ord(current_height)

        return height_diff < 2


def _parse(puzzle_input: str) -> HeightMap:
    heightmap = HeightMap()
    for y, line in enumerate(puzzle_input.splitlines()):
        heightmap.grid.append([])
        for x, char in enumerate(line):
            heightmap.grid[y].append(
                GridSquare(coordinates=(x, y), value=char),
            )

    return heightmap


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    heightmap = _parse(puzzle_input)

    print("Answer for part 1:", heightmap.find_shortest_path())


if __name__ == "__main__":
    main()
