def is_roll_accessible(row: int, col: int, grid: list) -> bool:
    min_row = max(row - 1, 0)
    max_row = min(row + 1, len(grid[row]) - 1)
    min_col = max(col - 1, 0)
    max_col = min(col + 1, len(grid) - 1)

    adjacent_rolls = 0
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if i == row and j == col:
                continue 
            if grid[i][j] == '@':
                adjacent_rolls += 1
    return adjacent_rolls < 4

def solution(filename: str) -> int:
    with open(filename, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    total_accessible_rolls = 0
    accessible_rolls = 1
    while accessible_rolls > 0:
        accessible_rolls = 0
        rolls_to_remove = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@' and is_roll_accessible(row, col, grid):
                    accessible_rolls += 1
                    rolls_to_remove.append((row, col))
        for row, col in rolls_to_remove:
            grid[row][col] = '.'
        total_accessible_rolls += accessible_rolls
    
    return total_accessible_rolls

if __name__ == "__main__":
    print(solution("day04/test.input"))
    print(solution("day04/main.input"))