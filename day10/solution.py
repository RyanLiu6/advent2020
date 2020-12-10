import os

def part_one():
    custom_adapter = CustomAdapter()

    return custom_adapter.count_part_one()

def part_two():
    custom_adapter = CustomAdapter()

    return custom_adapter.count_part_two()


class CustomAdapter:
    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.nums = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                self.nums.append(int(line))

        # Sort input
        self.nums.sort()
        self.built_in = max(self.nums)

    def count_part_one(self):
        ones = 0
        threes = 1

        start = 0
        for num in self.nums:
            diff = num - start

            if diff == 1:
                ones += 1

            if diff == 3:
                threes += 1

            start = num

        return ones * threes

    def count_part_two(self):
        pass
