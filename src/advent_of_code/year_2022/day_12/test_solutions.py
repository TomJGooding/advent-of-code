import pytest
from solutions import GridSquare, _load_puzzle_input, _parse


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_parse(example_data):
    heightmap = example_data
    assert heightmap.grid[0][0] == GridSquare(coordinates=(0, 0), value="S")
    assert heightmap.grid[4][7] == GridSquare(coordinates=(7, 4), value="i")
    assert heightmap.grid[2][5] == GridSquare(coordinates=(5, 2), value="E")


def test_heightmap_find_neighbours_of_corner_squares(example_data):
    heightmap = example_data
    assert heightmap.find_neighbours_of(
        GridSquare(
            coordinates=(0, 0),
            value="S",
        ),
    ) == [
        GridSquare(coordinates=(0, 1), value="a"),
        GridSquare(coordinates=(1, 0), value="a"),
    ]
    assert heightmap.find_neighbours_of(
        GridSquare(
            coordinates=(7, 4),
            value="i",
        ),
    ) == [
        GridSquare(coordinates=(7, 3), value="j"),
        GridSquare(coordinates=(6, 4), value="h"),
    ]


def test_heightmap_find_neighbours_of_edge_squares(example_data):
    heightmap = example_data
    assert heightmap.find_neighbours_of(
        GridSquare(
            coordinates=(2, 0),
            value="b",
        ),
    ) == [
        GridSquare(coordinates=(1, 0), value="a"),
        GridSquare(coordinates=(2, 1), value="c"),
        GridSquare(coordinates=(3, 0), value="q"),
    ]


def test_heightmap_find_neighbours_of_center_square(example_data):
    heightmap = example_data
    assert heightmap.find_neighbours_of(
        GridSquare(
            coordinates=(5, 2),
            value="E",
        ),
    ) == [
        GridSquare(coordinates=(5, 1), value="x"),
        GridSquare(coordinates=(4, 2), value="z"),
        GridSquare(coordinates=(5, 3), value="v"),
        GridSquare(coordinates=(6, 2), value="x"),
    ]


def test_heightmap_find_square_with_starting_value_S(example_data):
    heightmap = example_data
    assert heightmap.find_grid_square_with(value="S") == GridSquare(
        coordinates=(0, 0), value="S"
    )


def test_heightmap_can_move_to_lower_square(example_data):
    heightmap = example_data
    current_square = GridSquare(coordinates=(0, 0), value="z")
    neighbour = GridSquare(coordinates=(0, 1), value="m")
    assert heightmap._HeightMap__can_move(current_square, neighbour) is True


def test_heightmap_can_move_to_square_one_higher(example_data):
    heightmap = example_data
    current_square = GridSquare(coordinates=(0, 0), value="a")
    neighbour = GridSquare(coordinates=(0, 1), value="b")
    assert heightmap._HeightMap__can_move(current_square, neighbour) is True


def test_heightmap_can_move_to_square_same_level(example_data):
    heightmap = example_data
    current_square = GridSquare(coordinates=(0, 0), value="m")
    neighbour = GridSquare(coordinates=(0, 1), value="m")
    assert heightmap._HeightMap__can_move(current_square, neighbour) is True


def test_heightmap_can_move_to_square_two_higher_is_false(example_data):
    heightmap = example_data
    current_square = GridSquare(coordinates=(0, 0), value="a")
    neighbour = GridSquare(coordinates=(0, 1), value="m")
    assert heightmap._HeightMap__can_move(current_square, neighbour) is False


def test_heightmap_find_shortest_path(example_data):
    heightmap = example_data
    assert heightmap.find_shortest_path() == 31
