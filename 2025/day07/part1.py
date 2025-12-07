def solution(filename: str) -> int:
    with open(filename, "r") as file:
        diagram = [line.strip() for line in file]

    beam_path = {diagram[0].find("S")}

    splits = 0
    for level in range(2, len(diagram), 2):
        for beam in beam_path.copy():
            if diagram[level][beam] == "^":
                splits += 1
                beam_path.remove(beam)
                beam_path.add(beam + 1)
                beam_path.add(beam - 1)

    return splits


if __name__ == "__main__":
    expected = 21
    if (actual := solution("2025/day07/test.input")) == expected:
        print(solution("2025/day07/main.input"))
    else:
        print(f"{expected=}, {actual=}")
