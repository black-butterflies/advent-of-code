import math


def transpose(grid: list[str]) -> list[str]:
    trans_grid = ["" for _ in grid[0]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            trans_grid[j] += grid[i][j]

    return trans_grid


def result(problem: list[str]) -> int:
    operation = problem[0][-1]
    numbers = [int(problem[0][:-1].strip())]
    for n_str in problem[1:]:
        numbers.append(int(n_str.strip()))

    return sum(numbers) if operation == "+" else math.prod(numbers)


def solution(filename: str) -> int:
    with open(filename, "r") as file:
        homework = transpose([line.rstrip("\n") for line in file])

    total = 0
    curr_problem = []
    for s in homework:
        if s.strip():
            curr_problem.append(s)
        else:
            total += result(curr_problem)
            curr_problem = []
    total += result(curr_problem)

    return total


if __name__ == "__main__":
    expected = 3263827
    if (actual := solution("2025/day06/test.input")) == expected:
        print(solution("2025/day06/main.input"))
    else:
        print(f"{expected=}, {actual=}")
