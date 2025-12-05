def check_if_fresh(id_: int, fresh_ranges: list) -> bool:
    for min_id, max_id in fresh_ranges:
        if min_id <= id_ <= max_id:
            return True
    
    return False

def solution(filename: str) -> int:
    fresh_ranges = []
    fresh_checks = []
    with open(filename, "r") as file:
        ids = False
        for full_line in file:
            line = full_line.strip()
            if not line:
                ids = True
                continue
            if not ids:
                curr_range = tuple(map(int, line.split('-')))
                fresh_ranges.append(curr_range)
            else:
                fresh_checks.append(check_if_fresh(int(line), fresh_ranges))
    return sum(fresh_checks)

if __name__ == "__main__":
    print(solution("day05/test.input"))
    print(solution("day05/main.input"))