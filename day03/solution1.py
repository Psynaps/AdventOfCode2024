import re

with open("data", "r") as f:
    input = f.read()
    # print(input)
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    # print(matches)

    soln = 0
    for match in matches:
        a, b = int(match[0]), int(match[1])
        # print(a, b)
        soln += a * b
print(soln)
