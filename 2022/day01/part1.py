"""https://adventofcode.com/2022/day/1"""


def get_max_calories(filename: str) -> int:
    total = 0
    max_calories = total

    with open(filename, "r") as file:
        for line in file:
            clean = line.strip()
            if clean:
                total += int(clean)
            else:
                if total > max_calories:
                    max_calories = total
                total = 0

    return max_calories


print(get_max_calories("day01/main.input"))
