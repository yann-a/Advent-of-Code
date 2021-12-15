from aoc import AOC

aoc = AOC(13,  2021, __file__)

#input = aoc.get_example(1).strip().split('\n')
input = aoc.input.strip().split('\n')

# Read input
grid = set()
instructions = []

i = 0
while input[i] != '':
    grid.add((int(input[i].split(',')[0]), int(input[i].split(',')[1])))
    i += 1
i += 1
while i < len(input):
    instructions.append((input[i][11:].split('=')[0], int(input[i][11:].split('=')[1])))
    i += 1

# Apply a fold to grid


def apply(grid, instruction):
    direction, pos = instruction
    new_grid = set()

    for x, y in grid:
        if (direction == 'y' and y < pos) or (direction == 'x' and x < pos):
            new_grid.add((x, y))
        elif direction == 'y':
            new_grid.add((x, pos - (y - pos)))
        else:
            new_grid.add((pos - (x - pos), y))

    return new_grid

# Write result of fold to file


def show(grid):
    maxx, maxy = max([x for x, y in grid]), max([y for x, y in grid])

    gr = [[' ' for x in range(maxx + 1)] for x in range(maxy + 1)]
    for x, y in grid:
        if x >= 0 and y >= 0:
            gr[y][x] = '#'

    for line in gr:
        print(''.join(line))
    print()


# Execute instructions
# p1 is the result of first instruction
p1_sol = len(apply(grid, instructions[0]))
for instruction in instructions[1:]:
    grid = apply(grid, instruction)
show(grid)
p2_sol = 'BCZRCEAB'  # p2 is readable by a human in stdout

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
