def process_line(line):
    nums = list(map(int, line.split()))
    if len(nums) == 1:
        return 0

    isIncreasing = nums[0] < nums[1]
    for i, n in enumerate(nums[1:]):
        diff = 0
        if isIncreasing:
            if nums[i] >= n:
                return 0
            diff = n - nums[i]
        else:
            if nums[i] <= n:
                return 0
            diff = nums[i] - n
        if diff < 1 or diff > 3:
            return 0
    return 1


with open("data", "r") as f:
    lines = [line.strip() for line in f.readlines()]

count = 0
for line in lines:
    count += process_line(line)

print(count)
