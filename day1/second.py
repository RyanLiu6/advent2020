import os

def solution():
    nums = []
    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        for line in read_file:
            nums.append(int(line))

    (num_1, num_2, num_3) = three_sum(target=2020, nums=nums)

    print(num_1, num_2, num_3)

    return num_1 * num_2 * num_3

def three_sum(target, nums):
    # Naive solution - literally going to call two_sum within three_sum XD
    for num in nums:
        subtotal = target - num

        first, second = two_sum(subtotal, nums)

        if first + second == 0:
            continue
        else:
            return (num, first, second)

def two_sum(target, nums):
    # Should be guaranteed to find a counterpart
    for num in nums:
        counterpart = target - num
        if counterpart in nums:
            return (num, counterpart)

    return 0, 0
