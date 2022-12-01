from aoc import AOC
from collections import defaultdict

aoc = AOC(3,  2017, __file__)

input = 361527

square = 0
while input > (2 * square  + 1) ** 2:
    square += 1

layer_corners = [
    (2 * (square - 1) + 1) ** 2 + 2 * square,
    (2 * (square - 1) + 1) ** 2 + 4 * square,
    (2 * (square - 1) + 1) ** 2 + 6 * square,
    (2 * (square - 1) + 1) ** 2 + 8 * square
]
man_dist = 0
min_dist = 1_000_000

for corner in layer_corners:
    if abs(input - corner) < min_dist:
        man_dist = 2 * square - abs(input - corner)
        min_dist = abs(input - corner)

x = 1
y = 0
i = 2
square = 1
grid = defaultdict(int)
grid[(0, 0)] = 1
while True:
    grid[(x, y)] = sum([grid[(x + dx, y + dy)] for dx in range(-1, 2) for dy in range(-1, 2)])
    if grid[(x, y)] > input:
        break

    if i >= (2 * (square - 1) + 1) ** 2 + 6 * square:
        x += 1
        if i >= (2 * (square - 1) + 1) ** 2 + 8 * square:
            square += 1
    elif i >= (2 * (square - 1) + 1) ** 2 + 4 * square:
        y -= 1
    elif i >= (2 * (square - 1) + 1) ** 2 + 2 * square:
        x -= 1
    else:
        y += 1
    
    i += 1

p1_sol = man_dist
p2_sol = grid[(x, y)]

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)