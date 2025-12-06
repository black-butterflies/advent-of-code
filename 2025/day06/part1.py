import math


def solution(filename: str) -> int:
    with open(filename, "r") as file:
        homework = [line.split() for line in file]

    total = 0
    for col in range(len(homework[0])):
        operation = homework[-1][col]
        numbers = [int(homework[row][col]) for row in range(len(homework[:-1]))]
        total += sum(numbers) if operation == "+" else math.prod(numbers)

    return total


if __name__ == "__main__":
    expected = 4277556
    if (actual := solution("day06/test.input")) == expected:
        print(solution("day06/main.input"))
    else:
        print(f"{expected=}, {actual=}")
