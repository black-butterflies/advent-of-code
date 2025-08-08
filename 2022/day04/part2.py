"""https://adventofcode.com/2022/day/4#part2"""


def check_pairs(filename: str) -> None:
    pairs = 0
    with open(filename, "r") as file:
        for line in file:
            ranges = line.strip().split(",")
            section_limits = [
                int(limit) for section in ranges for limit in section.split("-")
            ]
            sec1 = set(range(section_limits[0], section_limits[1] + 1))
            sec2 = set(range(section_limits[2], section_limits[3] + 1))

            if not sec1.isdisjoint(sec2):
                pairs += 1

    print(f"total containing pairs = {pairs}")


check_pairs("day04/test.input")
check_pairs("day04/main.input")
