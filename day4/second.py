import os
import re

def solution():
    all_passports = []
    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        current_passport = []
        for line in read_file:
            curr = line.strip()

            if not curr:
                Passport.process_data(current_passport, all_passports)
                current_passport.clear()
            else:
                current_passport.append(curr)

        # Check at end if there's unprocessed stuff
        if len(current_passport) != 0:
            Passport.process_data(current_passport, all_passports)

    valid_passports = 0
    for passport in all_passports:
        if passport.is_valid():
            valid_passports += 1

    return valid_passports

class Passport:
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        # First check for Nones
        check = not any(i is None for i in (self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid))
        if not check:
            return False

        # Birth Year must be 4 digits, at least 1920 and at most 2002
        birth_year = int(self.byr)
        if len(self.byr) != 4 or birth_year < 1920 or birth_year > 2002:
            return False

        # Issue Year must be 4 digits and at least 2010 and at most 2020
        issue_year = int(self.iyr)
        if len(self.iyr) != 4 or issue_year < 2010 or issue_year > 2020:
            return False

        # Expiration Year must be 4 digits and at least 2020 and at most 2030
        expiration_year = int(self.eyr)
        if len(self.eyr) != 4 or expiration_year < 2020 or expiration_year > 2030:
            return False

        # Height must be a number followed by cm or in.
        # If cm, number must be at least 150 and at most 193
        # If in, number must be at least 59 and at most 76
        cm = "cm"
        inch = "in"

        if cm in self.hgt:
            height = self.hgt.split(cm)
            int_height = int(height[0])
            if int_height < 150 or int_height > 193:
                return False
        elif inch in self.hgt:
            height = self.hgt.split(inch)
            int_height = int(height[0])
            if int_height < 59 or int_height > 76:
                return False
        else:
            return False

        # Hair Colour must be start with # followed by exactly 6 characters 0-9 or a-f
        pattern = "^#[a-z0-9]{6}"
        result = re.match(pattern, self.hcl)
        if not result:
            return False

        # Eye Colour must be one of amb blu brn gry grn hzl oth
        valid_eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if not self.ecl in valid_eye_colours:
            return False

        # Passport ID must be a 9 digit number, including leading zeroes
        if len(self.pid) != 9:
            return False

        try:
            passport_id = int(self.pid)
        except ValueError:
            return False

        return True

    @staticmethod
    def process_data(values, output_list):
        passport_values = {}
        input_values = []

        for line in values:
            first = line.split()
            for item in first:
                second = item.split(":")
                passport_values[second[0]] = second[1]

        output_list.append(Passport(**passport_values))
