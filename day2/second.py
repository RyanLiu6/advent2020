import os

def solution():
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
