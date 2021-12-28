from aoc import AOC

aoc = AOC(22,  2016, __file__)

input = aoc.input.strip().split('\n')

nodes = {}
for line in input[2:]:
    line = line.split()

    name_split = line[0].split('-')
    x, y = int(name_split[1][1:]), int(name_split[2][1:])

    size, used, avail = int(line[1][:-1]), int(line[2][:-1]), int(line[3][:-1])
    nodes[(x, y)] = (used, avail, size)

nb_viable = 0
for (x1, y1) in nodes:
    for (x2, y2) in nodes:
        if (x1, y1) != (x2, y2):
            if 0 < nodes[(x1, y1)][0] <= nodes[(x2, y2)][1]:
                nb_viable += 1


for y in range(30):
    for x in range(34):
        if nodes[(x, y)][2] > 500:
            print('#', end=' ')
        elif nodes[(x, y)][0] == 0:
            print('_', end=' ')
        else:
            print('.', end=' ')
    print()

# P2: hacky, half-hardcoded solution, based on the map printed above
nb_steps = (17 - 7) + 6 + (32 - 7) # Move the empty node to the left of the data-bearing node
nb_steps += (1 + 4) * (33 - 1) # Move the data to the right of the (0, 0) node; and leave the (0, 0) node empty
nb_steps += 1 # Move the data to the (0, 0) node

p1_sol = nb_viable
p2_sol = nb_steps

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
