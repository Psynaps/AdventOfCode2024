with open("data", "r") as f:
    lines = [line.strip() for line in f.readlines()]


left = []
right = []
for line in lines:
    if len(line) == 0:
        break
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

soln = 0
for a, b in zip(left, right):
    soln += abs(a - b)

print(soln)
