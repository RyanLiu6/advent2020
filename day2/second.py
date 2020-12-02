import os

def solution():
    """
    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on.
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    How many passwords are valid according to the new interpretation of the policies?
    """
    passwords = []
    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        for line in read_file:
            values = line.split()

            policy = Policy(
                letter=values[1].split(":")[0],
                occurance=values[0])

            passwords.append(Password(policy, values[2]))

    valid = 0
    for password in passwords:
        if password.verify():
            valid += 1

    return valid


class Password:
    def __init__(self, policy, password):
        self.policy = policy
        self.password = password
        self.pos_dict = {}

        for k, v in enumerate(password):
            if v in self.pos_dict:
                self.pos_dict[v].append(k)
            else:
                self.pos_dict[v] = [k]

    def verify(self):
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
