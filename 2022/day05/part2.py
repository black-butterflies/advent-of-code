"""https://adventofcode.com/2022/day/5#part2"""


def parse_input(filename: str) -> None:
    with open(filename, "r") as file:
        first_line = file.readline()[:-1]
        n_stacks = get_number_of_cols(first_line)
        stacks = {str(i): [] for i in range(1, n_stacks + 1)}
        update_stacks(first_line, stacks)

        line = file.readline()
        while "[" in line:
            update_stacks(line, stacks)
            line = file.readline()

        # just outside the loop we have the line with the stack names
        file.readline()  # this is the empty line
        # now we can start parsing the movement lines
        for line in file:
            line_chunks = line.strip().split(" ")
            amount, stack_from, stack_to = line_chunks[1::2]
            make_move(stacks, int(amount), stack_from, stack_to)

    final_config = ""
    for i in range(1, n_stacks + 1):
        final_config += stacks[str(i)][0]

    print(f"final crate configuration: {final_config}")


def get_number_of_cols(file_string: str) -> int:
    length = len(file_string)

    return int((length + 1) / 4)


def update_stacks(file_string: str, stacks: dict) -> None:
    for i, pos in enumerate(range(1, len(file_string), 4)):
        if file_string[pos] != " ":
            stacks[str(i + 1)].append(file_string[pos])


def make_move(stacks: dict, amount: int, stack_from: str, stack_to: str) -> None:
    move_from, move_to = stacks[stack_from], stacks[stack_to]
    move_to[0:0] = move_from[:amount]
    stacks[stack_from] = move_from[amount:]


parse_input("day05/test.input")
parse_input("day05/main.input")
