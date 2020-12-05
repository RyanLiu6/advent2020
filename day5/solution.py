import os
import re

def part_one():
    custom_boarding_pass = CustomBoardingPass()

    return custom_boarding_pass.process_part_one()

def part_two():
    custom_boarding_pass = CustomBoardingPass()

    return custom_boarding_pass.process_part_two()


class CustomBoardingPass:
    def __init__(self):
        self.parse_input()

    def parse_input(self):
        self.boarding_passes = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                current = line.strip()
                self.boarding_passes.append(BoardingPass(current))

    def process_part_one_iter(self):
        max_seat_id = 0

        for item in self.boarding_passes:
            current_seat_id = item.get_seat_id()
            if current_seat_id > max_seat_id:
                max_seat_id = current_seat_id

        return max_seat_id

    def process_part_one(self):
        seat_ids = [item.get_seat_id() for item in self.boarding_passes]

        return max(seat_ids)

    def process_part_two(self):
        # We know that there's rows 0 - 127 and columns 0 - 7
        seats = [[False for i in range(8)] for j in range(128)]

        for item in self.boarding_passes:
            seats[item.row][item.column] = True

        # Seat isn't in very front or back
        # Seats with IDs +1 and -1 will be in list of taken seats
        empty_seats = {}
        for i in range(128):
            for j in range(8):
                if not seats[i][j]:
                    if i in empty_seats:
                        empty_seats[i].append((i, j))
                    else:
                        empty_seats[i] = [(i, j)]

        """
        Remove more seats at the front or back by looking at sets of seats
        that repeat ie (127, 0), (127, 1) ...
        """
        front_and_back = [0, 127]
        for k, v in empty_seats.items():
            if k not in front_and_back:
                # Check how many elements are there, if more than one we can throw it away
                if len(v) > 1:
                    continue
                else:
                    # Found it!
                    return BoardingPass.calculate_seat_id(v[0][0], v[0][1])

        return 0

class BoardingPass:
    def __init__(self, string):
        self.row_start = 0
        self.row_end = 127

        self.column_start = 0
        self.column_end = 7

        self.string = string

        # no validation for other one
        self.F = "F"
        self.L = "L"

        self._process_data()

    def _process_data(self):
        # First seven describe row
        for i in range(7):
            val = self.string[i]
            if val == self.F:
                self.row_end = (self.row_start + self.row_end) // 2
            else:
                self.row_start = (self.row_start + self.row_end) // 2 + 1

        # Next three describe column
        for i in range(3):
            val = self.string[i + 7]
            if val == self.L:
                self.column_end = (self.column_start + self.column_end) // 2
            else:
                self.column_start = (self.column_start + self.column_end) // 2 + 1

        # At this point row_start == row_end and column_start == column_end
        self.row = self.row_end
        self.column = self.column_end

    def get_seat_id(self):
        return BoardingPass.calculate_seat_id(self.row, self.column)

    @staticmethod
    def calculate_seat_id(row, column):
        return row * 8 + column
