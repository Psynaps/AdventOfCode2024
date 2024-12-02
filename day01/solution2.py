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
for n in left:
    soln += n * right.count(n)

print(soln)
