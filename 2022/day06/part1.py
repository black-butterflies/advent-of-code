"""https://adventofcode.com/2022/day/6"""


def parse_input(filename: str) -> None:
    with open(filename, "r") as file:
        for line in file:
            processed_chars = find_marker(line.strip())
            print(f"first marker after character {processed_chars}")


def find_marker(buffer: str) -> int:
    for i in range(len(buffer) - 4 + 1):
        last_4 = buffer[i : i + 4]
        if len(set(last_4)) == 4:
            return i + 4


parse_input("day06/test.input")
parse_input("day06/main.input")
