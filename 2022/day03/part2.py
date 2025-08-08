"""https://adventofcode.com/2022/day/3#part2"""

import string


def parse_input(filename: str) -> int:
    total_priority = 0
    with open(filename, "r") as file:
        group_rucksacks = []
        for idx, line in enumerate(file):
            if idx % 3 == 2:
                group_rucksacks.append(line.strip())
                common = find_common_element(group_rucksacks)
                total_priority += get_priority(common)
                group_rucksacks = list()
            else:
                group_rucksacks.append(line.strip())

    print(f"priority sum = {total_priority}")


def find_common_element(group_rucksacks: list[str]) -> str:
    rucksack_sets = [set(rucksack) for rucksack in group_rucksacks]
    intersection = set.intersection(*rucksack_sets)

    return tuple(intersection)[0]


def get_priority(letter: str) -> int:
    alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    return alphabets.index(letter) + 1


parse_input("day03/test.input")
parse_input("day03/main.input")
