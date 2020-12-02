import os

def solution():
    """
    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each line gives the password policy and then the password.
    The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.

    For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid.
    The middle password, cdefg, is not; it contains no instances of b, but needs at least 1.
    The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

    How many passwords are valid according to their policies?
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
        self.freq_dict = {}

        for letter in password:
            if letter in self.freq_dict:
                self.freq_dict[letter] += 1
            else:
                self.freq_dict[letter] = 1

    def verify(self):
        try:
            occurances = self.freq_dict[self.policy.letter]
            return (occurances >= self.policy.min) and (occurances <= self.policy.max)
        except KeyError:
            return False


class Policy(object):
    def __init__(self, letter, occurance):
        occurances = occurance.split("-")

        self.letter = letter
        self.min = int(occurances[0])
        self.max = int(occurances[1])
