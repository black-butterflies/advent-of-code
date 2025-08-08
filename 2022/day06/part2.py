"""https://adventofcode.com/2022/day/6#part2"""


def parse_input(filename: str) -> None:
    with open(filename, "r") as file:
        for line in file:
            processed_chars = find_message(line.strip())
            print(f"first marker after character {processed_chars}")


def find_message(buffer: str) -> int:
    window = 14
    for i in range(len(buffer) - window + 1):
        last_4 = buffer[i : i + window]
        if len(set(last_4)) == window:
            return i + window


parse_input("day06/test.input")
parse_input("day06/main.input")
