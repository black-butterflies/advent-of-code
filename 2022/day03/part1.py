"""https://adventofcode.com/2022/day/3"""

import string


def parse_input(filename: str) -> int:
    total_priority = 0
    with open(filename, "r") as file:
        for line in file:
            common = find_common_element(line.strip())[0]
            total_priority += get_priority(common)

    print(f"priority sum = {total_priority}")


def find_common_element(rucksack: str) -> tuple[str]:
    mid = len(rucksack) // 2
    comp1 = set(rucksack[:mid])
    comp2 = set(rucksack[mid:])

    return tuple(comp1.intersection(comp2))


def get_priority(letter: str) -> int:
    alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    return alphabets.index(letter) + 1


parse_input("day03/test.input")
parse_input("day03/main.input")
