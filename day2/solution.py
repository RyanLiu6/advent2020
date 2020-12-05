import os
import re

def part_one():
    custom_password = CustomPassword()

    return custom_password.count_part_one()

def part_two():
    custom_password = CustomPassword()

    return custom_password.count_part_two()


class CustomPassword:
    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.passwords = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                values = line.split()

                policy = Policy(
                    letter=values[1].split(":")[0],
                    occurance=values[0])

                self.passwords.append(Password(policy, values[2]))

    def count_part_one(self):
        valid = 0
        for password in self.passwords:
            if password.verify_part_one():
                valid += 1

        return valid

    def count_part_two(self):
        valid = 0
        for password in self.passwords:
            if password.verify_part_two():
                valid += 1

        return valid


class Password:
    def __init__(self, policy, password):
        self.policy = policy
        self.password = password

        # Details for part one
        self.freq_dict = {}
        for letter in password:
            if letter in self.freq_dict:
                self.freq_dict[letter] += 1
            else:
                self.freq_dict[letter] = 1

        # Details for part two
        self.pos_dict = {}
        for k, v in enumerate(password):
            if v in self.pos_dict:
                self.pos_dict[v].append(k)
            else:
                self.pos_dict[v] = [k]

    def verify_part_one(self):
        try:
            occurances = self.freq_dict[self.policy.letter]
            return (occurances >= self.policy.min) and (occurances <= self.policy.max)
        except KeyError:
            return False

    def verify_part_two(self):
        has_occured = False

        try:
            keys = self.pos_dict[self.policy.letter]
        except KeyError:
            return False

        if self.policy.min - 1 in keys:
            has_occured = not has_occured

        if self.policy.max - 1 in keys:
            has_occured = not has_occured

        return has_occured


class Policy(object):
    def __init__(self, letter, occurance):
        occurances = occurance.split("-")

        self.letter = letter
        self.min = int(occurances[0])
        self.max = int(occurances[1])
