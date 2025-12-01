def solution(filename: str) -> int:
    with open(filename, "r") as f:
        pos = 50
        count = 0
        for line in f:
            direction = line[0]
            distance = int(line.strip()[1:])
            pos = (pos + distance * (1 if direction == "R" else -1)) % 100
            if pos == 0:
                count += 1
    return count


if __name__ == "__main__":
    print(solution("day01/test.input"))
    print(solution("day01/main.input"))
