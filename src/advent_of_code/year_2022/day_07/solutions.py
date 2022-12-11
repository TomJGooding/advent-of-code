from pathlib import Path
from typing import Optional

PUZZLE_TITLE: str = "--- Day 7: No Space Left On Device ---"
PUZZLE_DIR = Path(__file__).parent


def _load_puzzle_input(filename: Optional[str] = None) -> str:
    if not filename:
        filename = "input.txt"
    return (PUZZLE_DIR / filename).read_text().strip()


class Directory:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.subdirectories: list[Directory] = []
        self.files: list[File] = []

    @property
    def name(self) -> str:
        if self.path == "/":
            return self.path
        else:
            return self.path.rsplit("/", maxsplit=1)[1]

    @property
    def parent_path(self) -> str:
        parent_path: str = self.path.rsplit("/", maxsplit=1)[0]
        if self.path != "/" and not parent_path:
            parent_path = "/"
        return parent_path

    @property
    def size(self) -> int:
        file_sizes: list[int] = [file.size for file in self.files]
        subdirectory_sizes: list[int] = [
            subdirectory.size for subdirectory in self.subdirectories
        ]
        return sum(file_sizes + subdirectory_sizes)


class File:
    def __init__(self, path: str, size: int) -> None:
        self.path: str = path
        self.size: int = size

    @property
    def directory(self) -> str:
        directory: str = self.path.rsplit("/", maxsplit=1)[0]
        if not directory:
            directory = "/"
        return directory


def _parse(puzzle_input: str) -> list[Directory]:
    cwd_path: str = ""
    directories: list[Directory] = []
    for line in puzzle_input.splitlines():
        if line == "$ ls":
            continue
        elif line.startswith("$ cd"):
            cd_param: str = line.rsplit(" ", maxsplit=1)[1]
            # change cwd
            cwd_path = _change_cwd_path(cd_param, cwd_path)
            # create empty directory
            if cd_param != "..":
                directories.append(Directory(cwd_path))
        elif not line.startswith("dir "):
            # create file and add to directory
            file: File = _create_file(file_listing=line, cwd_path=cwd_path)
            for directory in directories:
                if directory.path == cwd_path:
                    directory.files.append(file)

    # add subdirectories to directories
    for directory in directories:
        for subdirectory in directories:
            if directory.path == subdirectory.parent_path:
                directory.subdirectories.append(subdirectory)

    return directories


def _change_cwd_path(cd_param: str, cwd_path: str) -> str:
    new_cwd_path: str
    if cd_param == "/":
        new_cwd_path = "/"
    elif cd_param == "..":
        new_cwd_path = cwd_path.rsplit("/", maxsplit=1)[0]
        if not new_cwd_path:
            new_cwd_path = "/"
    elif cwd_path == "/":
        new_cwd_path = cwd_path + cd_param
    else:
        new_cwd_path = "/".join((cwd_path, cd_param))

    return new_cwd_path


def _create_file(file_listing: str, cwd_path: str) -> File:
    size: int = int(file_listing.split()[0])
    name: str = file_listing.split()[1]
    path: str = cwd_path + name if cwd_path == "/" else "/".join((cwd_path, name))
    return File(path, size)


def _filter_directories_by_size(
    max_size: int, directories: list[Directory]
) -> list[Directory]:
    return [dir for dir in directories if dir.size <= max_size]


def main() -> None:
    print(PUZZLE_TITLE)
    puzzle_input: str = _load_puzzle_input("input.txt")
    directories = _parse(puzzle_input)
    print(
        "Answer for part 1: ",
        sum(
            [
                dir.size
                for dir in _filter_directories_by_size(
                    100000,
                    directories,
                )
            ]
        ),
    )


if __name__ == "__main__":
    main()
