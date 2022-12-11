import pytest
from solutions import (
    Directory,
    _available_disk_space,
    _filter_directories_by_size,
    _load_puzzle_input,
    _parse,
)


@pytest.fixture
def example_data():
    example_input = _load_puzzle_input(filename="example.txt")
    return _parse(example_input)


def test_directory_class():
    directory = Directory("/a/b/c")
    assert directory.path == "/a/b/c"
    assert directory.name == "c"
    assert directory.parent_path == "/a/b"


def test_directory_class_when_parent_is_root():
    directory = Directory("/a")
    assert directory.path == "/a"
    assert directory.name == "a"
    assert directory.parent_path == "/"


def test_directory_class_when_is_root():
    directory = Directory("/")
    assert directory.path == "/"
    assert directory.name == "/"
    assert not directory.parent_path


def test_parse_creates_correct_directories(example_data):
    actual = [directory.path for directory in example_data]
    expected = ["/", "/a", "/a/e", "/d"]
    assert actual == expected


def test_parse_adds_files_to_correct_directories(example_data):
    actual = [
        (directory.path, [file.path for file in directory.files])
        for directory in example_data
    ]
    expected = [
        ("/", ["/b.txt", "/c.dat"]),
        ("/a", ["/a/f", "/a/g", "/a/h.lst"]),
        ("/a/e", ["/a/e/i"]),
        ("/d", ["/d/j", "/d/d.log", "/d/d.ext", "/d/k"]),
    ]
    assert actual == expected


def test_parse_adds_correct_subdirectories(example_data):
    actual = [
        (directory.path, [subdir.path for subdir in directory.subdirectories])
        for directory in example_data
    ]
    expected = [
        ("/", ["/a", "/d"]),
        ("/a", ["/a/e"]),
        ("/a/e", []),
        ("/d", []),
    ]
    assert actual == expected


def test_parse_directories_have_correct_sizes(example_data):
    actual = [(directory.path, directory.size) for directory in example_data]
    expected = [
        ("/", 48381165),
        ("/a", 94853),
        ("/a/e", 584),
        ("/d", 24933642),
    ]
    assert actual == expected


def test_filter_directories_by_size(example_data):
    actual = [
        dir.path
        for dir in _filter_directories_by_size(
            max_size=100000, directories=example_data
        )
    ]
    expected = ["/a", "/a/e"]
    assert actual == expected


def test_available_disk_space(example_data):
    assert _available_disk_space(example_data) == 21618835
