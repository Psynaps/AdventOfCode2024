def count_completions():
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "X":
                for move_r, move_c in moves:
                    total += count_completions_helper(r, c, move_r, move_c)
    return total


def count_completions_helper(start_r, start_c, dir_r, dir_c):
    limit_r = start_r + (3 * dir_r)
    limit_c = start_c + (3 * dir_c)
    if limit_r < 0 or limit_r >= len(lines) or limit_c < 0 or limit_c >= len(lines[0]):
        return 0
    if (
        lines[start_r][start_c] == "X"
        and lines[start_r + (1 * dir_r)][start_c + (1 * dir_c)] == "M"
        and lines[start_r + (2 * dir_r)][start_c + (2 * dir_c)] == "A"
        and lines[start_r + (3 * dir_r)][start_c + (3 * dir_c)] == "S"
    ):
        return 1
    return 0


with open("data", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    print(count_completions())
