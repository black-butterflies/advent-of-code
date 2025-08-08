"""https://adventofcode.com/2022/day/2#part2"""


def get_total_score(filename: str) -> None:
    decrypted_guide = {"A": 0, "B": 1, "C": 2}
    total_score = 0
    with open(filename, "r") as file:
        for line in file:
            opp_letter, result = line.strip().split(" ")
            opponent = decrypted_guide[opp_letter]
            if result == "X":
                player = (opponent - 1) % 3
            elif result == "Y":
                player = opponent
            elif result == "Z":
                player = (opponent + 1) % 3
            total_score += get_score(player, opponent)

    print(f"total score = {total_score}")


def get_score(player: int, opponent: int) -> int:
    shape_score = player + 1

    # draw
    if player == opponent:
        return shape_score + 3
    # player wins
    elif opponent == (player - 1) % 3:
        return shape_score + 6
    # opponent wins
    else:
        return shape_score


get_total_score("day02/test.input")
get_total_score("day02/main.input")
