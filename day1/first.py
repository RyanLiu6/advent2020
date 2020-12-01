import os

def solution():
    """
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456

    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
    """
    nums = []
    with open(os.path.join(os.path.abspath(os.getcwd()), "first.txt")) as read_file:
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

