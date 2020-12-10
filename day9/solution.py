import os

def part_one():
    custom_encoding = CustomEncoding()

    return custom_encoding.process_part_one()

def part_two():
    custom_encoding = CustomEncoding()

    return custom_encoding.process_part_two()


class CustomEncoding:
    def __init__(self):
        self.preamble = 25

        self.parse_input()

    def parse_input(self):
        self.nums = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                self.nums.append(int(line))

    def process_part_one(self):
        counter = 0
        for i in range(self.preamble, len(self.nums)):
            val = self.nums[i]
            prev_25 = self.nums[counter:counter + self.preamble]
            counter += 1

            if not self.two_sum(val, prev_25):
                return val

    def process_part_two(self):
        problematic_number = self.process_part_one()
        start, end = self.sliding_window(problematic_number)

        cont_arr = self.nums[start:end+1]

        return min(cont_arr) + max(cont_arr)

    def two_sum(self, target, arr):
        for num in arr:
            counterpart = target - num
            if counterpart in arr:
                return True

        return False

    def sliding_window(self, target):
        start, end = 0, 0

        while True:
            total = sum(self.nums[start:end + 1])

            if total == target:
                return (start, end)
            elif total < target:
                end += 1
            else:
                start += 1
