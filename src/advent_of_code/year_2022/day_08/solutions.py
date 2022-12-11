from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 8: Treetop Tree House ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


def _parse(puzzle_input: str) -> list[list[int]]:
    data: list[list[int]] = []
    for line in puzzle_input.splitlines():
        data.append([int(tree) for tree in line])
    return data


def _total_visible_trees(trees_grid: list[list[int]]) -> int:
    corners: int = 4
    grid_width: int = len(trees_grid[0])
    grid_height: int = len(trees_grid)

    count: int = (grid_height * 2) + (grid_height * 2) - corners
    for row_idx in range(1, grid_height - 1):
        for col_idx in range(1, grid_width - 1):
            if _tree_is_visible(row_idx, col_idx, trees_grid):
                count += 1

    return count


def _trees_right(
    trees_grid: list[list[int]],
    row_idx: int,
    col_idx: int,
) -> list[int]:
    grid_width: int = len(trees_grid[0])
    return trees_grid[row_idx][col_idx + 1 : grid_width]


def _trees_left(
    trees_grid: list[list[int]],
    row_idx: int,
    col_idx: int,
) -> list[int]:
    return trees_grid[row_idx][0:col_idx]


def _trees_above(
    trees_grid: list[list[int]],
    row_idx: int,
    col_idx: int,
) -> list[int]:
    return [row[col_idx] for row in trees_grid[0:row_idx]]


def _trees_below(
    trees_grid: list[list[int]],
    row_idx: int,
    col_idx: int,
) -> list[int]:
    grid_height: int = len(trees_grid)
    return [row[col_idx] for row in trees_grid[row_idx + 1 : grid_height]]


def _tree_is_visible(
    row_idx: int,
    col_idx: int,
    trees_grid: list[list[int]],
) -> bool:
    current_tree: int = trees_grid[row_idx][col_idx]
    tallest_surrounding_trees: list[int] = [
        max(_trees_right(trees_grid, row_idx, col_idx)),
        max(_trees_left(trees_grid, row_idx, col_idx)),
        max(_trees_above(trees_grid, row_idx, col_idx)),
        max(_trees_below(trees_grid, row_idx, col_idx)),
    ]

    return any(tree < current_tree for tree in tallest_surrounding_trees)


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    trees_grid = _parse(puzzle_input)
    print(f"Answer for part 1: {_total_visible_trees(trees_grid)}")


if __name__ == "__main__":
    main()
