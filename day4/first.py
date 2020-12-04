import os

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
        return not any(i is None for i in (self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid))

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
