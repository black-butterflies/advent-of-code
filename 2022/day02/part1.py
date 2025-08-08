"""https://adventofcode.com/2022/day/2"""


def get_total_score(filename: str) -> None:
    decrypted_guide = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    total_score = 0
    with open(filename, "r") as file:
        for line in file:
            player, opponent = (
                decrypted_guide[letter] for letter in line.strip().split(" ")
            )
            total_score += get_score(player, opponent)

    print(f"total score = {total_score}")


def get_score(opponent: int, player: int) -> int:
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


get_total_score("day02/main.input")
