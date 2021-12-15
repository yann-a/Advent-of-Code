def won(grid, drawn):
    """
    returns True iff grid is a bingo with the numbers from drawn
    """
    for line in range(len(grid)):
        lineisok = True
        for row in range(len(grid[0])):
            if grid[line][row] not in drawn:
                lineisok = False
        if lineisok:
            return True

    for row in range(len(grid[0])):
        lineisok = True
        for line in range(len(grid)):
            if grid[line][row] not in drawn:
                lineisok = False
        if lineisok:
            return True

    return False


def score(grid, drawn):
    """ returns the score of a grid with the numbers from drawn """
    return sum([x for l in grid for x in l if x not in drawn])


with open('input', 'r') as f:
    draw = list(map(int, f.readline().split(',')))  # Get drawn numbers
    f.readline()  # Discard empty line

    # Get grids
    grids = []
    grid = []
    while True:
        l = list(map(int, f.readline().strip().split()))  # Read line
        if len(l) == 0:  # If empty line, two case: either the end: or a sep between two grids
            if len(grid) == 0:  # If end, break
                break
            grids.append(grid)  # Else add grid to the list of grids
            grid = []
        else:  # Continue reading the current grid
            grid.append(l)

    # Solve challenges
    i = 1  # Start with the first number
    has_won, nb_won = [False] * len(grids), 0  # keep track of solved grids
    while nb_won < len(grids):
        for k, grid in enumerate(grids):  # go through each unsolved grid
            if not has_won[k]:
                if won(grid, draw[:i]):
                    has_won[k] = True
                    nb_won += 1

                    if nb_won == 1:
                        print('Part 1:', draw[i-1] * score(grid, draw[:i]))
                    if nb_won == len(grids):
                        print('Part 2:', draw[i-1] * score(grid, draw[:i]))
        i += 1  # Draw an additional number
