import os
import enum

def part_one():
    custom_instructions = CustomInstructions()

    return custom_instructions.count_part_one()[0]

def part_two():
    custom_instructions = CustomInstructions()

    return custom_instructions.count_part_two()


class CustomInstructions:
    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.instructions = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                self.instructions.append(Instructions(line.strip()))

    def count_part_one(self):
        index = 0
        accumulator = 0

        for item in self.instructions:
            item.has_processed = False

        while index < len(self.instructions) and not self.instructions[index].has_processed:
            item = self.instructions[index]
            item.has_processed = True

            if item.type == Instructions.ACC:
                accumulator += item.value
            elif item.type == Instructions.JMP:
                # -1 here b/c we increment by 1 at the end
                index += item.value - 1

            index += 1

        return accumulator, index == len(self.instructions)

    def count_part_two(self):
        for item in self.instructions:
            if item.type == Instructions.JMP or item.type == Instructions.NOP:
                item.flip_type()

                accumulator, complete = self.count_part_one()

                item.flip_type()

                if complete:
                    return accumulator


class Instructions:
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"

    def __init__(self, string):
        data = string.split()

        self.type = None
        if data[0] == self.ACC:
            self.type = self.ACC
        elif data[0] == self.JMP:
            self.type = self.JMP
        else:
            self.type = self.NOP

        # Native support for negative and positive numbers
        self.value = int(data[1])

        # For keeping track
        self.has_processed = False

    def __str__(self):
        return f"{self.type} {self.value}"

    def process(self):
        if self.type == self.ACC:
            return self.value
        else:
            return 0

    def flip_type(self):
        if self.type == self.NOP:
            self.type = self.JMP
        else:
            self.type = self.NOP
