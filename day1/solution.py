import os

def part_one():
    custom_sum = CustomSum()

    (num_1, num_2) = custom_sum.two_sum(target=2020)
    print(num_1, num_2)

    return num_1 * num_2

def part_two():
    custom_sum = CustomSum()

    (num_1, num_2, num_3) = custom_sum.three_sum(target=2020)

    print(num_1, num_2, num_3)

    return num_1 * num_2 * num_3


class CustomSum:
    def __init__(self):
        self.parse_input()

    def two_sum(self, target):
        # Guaranteed to find a counterpart
        for num in self.nums:
            counterpart = target - num
            if counterpart in self.nums:
                return (num, counterpart)

        return 0, 0

    def three_sum(self, target):
        # Naive solution - literally going to call two_sum within three_sum XD
        for num in self.nums:
            subtotal = target - num

            first, second = self.two_sum(subtotal)

            if first + second == 0:
                continue
            else:
                return (num, first, second)

    def parse_input(self):
        self.nums = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                self.nums.append(int(line))
