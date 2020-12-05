import os

def part_one():
    custom_board = CustomBoard()

    return custom_board.board_crawler(3, 1)

def part_two():
    results = []
    custom_board = CustomBoard()

    # Right 1, down 1.
    results.append(custom_board.board_crawler(1, 1))

    # Right 3, down 1.
    results.append(custom_board.board_crawler(3, 1))

    # Right 5, down 1.
    results.append(custom_board.board_crawler(5, 1))

    # Right 7, down 1.
    results.append(custom_board.board_crawler(7, 1))

    # Right 1, down 2.
    results.append(custom_board.board_crawler(1, 2))

    total = 1
    for item in results:
        total *= item

    return total


class CustomBoard:
    def __init__(self):
        self.parse_input()

        self.height = len(self.puzzle_map)
        self.width = len(self.puzzle_map[0])

        self.trees = "#"

    def parse_input(self):
        separator =  "/"
        self.puzzle_map = []
        with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
            for line in read_file:
                self.puzzle_map.append(separator.join(line.strip()).split(separator))

    def board_crawler(self, right, down):
        i, j = 0, 0
        trees_hit = 0

        while i < self.height:
            current = self.puzzle_map[i][j]
            if self.is_tree(current):
                trees_hit += 1

            j = (j + right) % self.width
            i += down

        return trees_hit

    def is_tree(self, char):
        return char == self.trees
