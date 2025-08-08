"""https://adventofcode.com/2022/day/1#part2"""


def get_top3_calories(filename: str) -> tuple[int, int, int]:
    total = 0
    top1 = total
    top2 = total
    top3 = total

    with open(filename, "r") as file:
        for line in file:
            clean = line.strip()
            if clean:
                total += int(clean)
            else:
                if total > top3:
                    if total > top1:
                        top1, top2, top3 = total, top1, top2
                    elif total > top2:
                        top2, top3 = total, top2
                    else:
                        top3 = total
                total = 0

    return top1, top2, top3


elves_top3 = get_top3_calories("day01/main.input")
print(f"Top 3 calories: {elves_top3}")
print(f"Total calories: {sum(elves_top3)}")
