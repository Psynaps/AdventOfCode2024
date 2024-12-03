def process_line(line):
    nums = list(map(int, line.split()))
    if sequence_valid(nums):
        return 1

    # See if each sequence made by removing one element is valid
    #
    # Could definitely dynamic programming solve this with subproblems
    # being: subarrays being valid increasing or decreasing
    for i in range(len(nums)):
        if sequence_valid(nums[:i] + nums[i + 1 :]):
            return 1
    return 0


def sequence_valid(nums):
    if len(nums) == 1:
        return 0

    faults_increasing = 0
    faults_decreasing = 0

    for i, n in enumerate(nums[1:]):
        diff = n - nums[i]  # i is index into nums[1:], so n = nums[i+1]
        if diff < 1 or diff > 3:
            faults_increasing += 1
        if diff > -1 or diff < -3:
            faults_decreasing += 1

    return int(faults_increasing == 0 or faults_decreasing == 0)


with open("data", "r") as f:
    lines = [line.strip() for line in f.readlines()]

count = 0
for line in lines:
    res = process_line(line)
    count += res

print(count)
