import os

def solution():
    puzzle_map = []

    separator =  "/"

    with open(os.path.join(os.path.abspath(os.getcwd()), "input.txt")) as read_file:
        for line in read_file:
            puzzle_map.append(separator.join(line.strip()).split(separator))

    results = []

    # Right 1, down 1.
    results.append(_solution_helper(puzzle_map, 1, 1))

    # Right 3, down 1.
    results.append(_solution_helper(puzzle_map, 3, 1))

    # Right 5, down 1.
    results.append(_solution_helper(puzzle_map, 5, 1))

    # Right 7, down 1.
    results.append(_solution_helper(puzzle_map, 7, 1))

    # Right 1, down 2.
    results.append(_solution_helper(puzzle_map, 1, 2))

    total = 1
    for item in results:
        total *= item

    return total

def _solution_helper(puzzle_map, right, down):
    trees = "#"
    empty = "."

    trees_hit = 0
    height = len(puzzle_map)
    width = len(puzzle_map[0])

    i, j = 0, 0

    while i < height:
        current = puzzle_map[i][j]
        if is_tree(current):
            trees_hit += 1

        j = (j + right) % width
        i += down

    return trees_hit


def is_tree(char):
    return char == "#"

def is_empty(char):
    return char == "."
