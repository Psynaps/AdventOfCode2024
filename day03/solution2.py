import re

with open("data", "r") as f:
    input = f"do(){f.read()}don't()"

    soln = 0
    enabled = False
    segments = re.split(r"(do\(\)|don't\(\))", input)

    for segment in segments:
        if segment == "do()":
            enabled = True
        elif segment == "don't()":
            enabled = False
        elif enabled:
            muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", segment)
            for mul in muls:
                a, b = int(mul[0]), int(mul[1])
                soln += a * b

print(soln)
