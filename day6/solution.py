import os

def part_one():
    custom_customs = CustomCustoms()

    return custom_customs.count_part_one()

def part_two():
    custom_customs = CustomCustoms()

    return custom_customs.count_part_two()


class CustomCustoms:
    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.customs = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            current_customs = []
            for line in read_file:
                curr = line.strip()

                if not curr:
                    self.customs.append(Customs(current_customs))
                    current_customs.clear()
                else:
                    current_customs.append(curr)

            # Check at end if there's unprocessed stuff
            if len(current_customs) != 0:
                self.customs.append(Customs(current_customs))

    def count_part_one(self):
        total = 0

        for item in self.customs:
            total += item.sum_part_one()

        return total

    def count_part_two(self):
        total = 0

        for item in self.customs:
            total += item.sum_part_two()

        return total


class Customs:
    def __init__(self, lines):
        self.lines = lines
        self.num_people = len(lines)

        self._process_data()

    def _process_data(self):
        self.key_map = {}

        for line in self.lines:
            for char in line:
                try:
                    self.key_map[char] += 1
                except KeyError:
                    self.key_map[char] = 1

    def sum_part_one(self):
        return len(self.key_map.keys())

    def sum_part_two(self):
        total = 0
        for val in self.key_map.values():
            if val == self.num_people:
                total += 1

        return total
