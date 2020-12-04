import os

def solution():
    nums = []
    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        for line in read_file:
            nums.append(int(line))

    (num_1, num_2) = two_sum(target=2020, nums=nums)

    print(num_1, num_2)

    return num_1 * num_2

def two_sum(target, nums):
    # Should be guaranteed to find a counterpart
    for num in nums:
        counterpart = target - num
        if counterpart in nums:
            return (num, counterpart)

    return 0, 0

