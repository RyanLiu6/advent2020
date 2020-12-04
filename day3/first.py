import os

def solution():
    puzzle_map = []

    separator =  "/"

    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        for line in read_file:
            puzzle_map.append(separator.join(line.strip()).split(separator))

    trees = "#"
    empty = "."

    trees_hit = 0
    height = len(puzzle_map)
    width = len(puzzle_map[0])

    i, j = 0, 0

    # Pattern is right 3 and down 1
    while i < height:
        current = puzzle_map[i][j]
        if is_tree(current):
            trees_hit += 1

        j = (j + 3) % width
        i += 1

    return trees_hit

def is_tree(char):
    return char == "#"

def is_empty(char):
    return char == "."
