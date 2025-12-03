def solution(filename: str) -> int:
    with open(filename, "r") as file:
        total = 0
        for line in file:
            max_joltage = 0
            for i, char in enumerate(line.strip()[:-1]):
                curr_joltage = int(char) * 10
                for char2 in line.strip()[i+1:]:
                    curr_joltage = int(char) * 10 + int(char2)
                    if curr_joltage > max_joltage:
                        max_joltage = curr_joltage
            total += max_joltage

    return total

if __name__ == "__main__":
    print(solution("day03/test.input"))
    print(solution("day03/main.input"))