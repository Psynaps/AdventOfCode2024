def count_completions():
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "A":
                total += count_completions_helper(r, c)
    return total


def count_completions_helper(start_r, start_c):
    if (
        start_r < 1
        or start_r >= (len(lines) - 1)
        or start_c < 1
        or start_c >= (len(lines[0]) - 1)
    ):
        return 0

    if (
        lines[start_r - 1][start_c - 1] == "M"
        and lines[start_r + 1][start_c + 1] == "S"
    ) or (
        lines[start_r - 1][start_c - 1] == "S"
        and lines[start_r + 1][start_c + 1] == "M"
    ):
        if (
            lines[start_r - 1][start_c + 1] == "M"
            and lines[start_r + 1][start_c - 1] == "S"
        ) or (
            lines[start_r - 1][start_c + 1] == "S"
            and lines[start_r + 1][start_c - 1] == "M"
        ):
            return 1
    return 0


with open("data", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    print(count_completions())
