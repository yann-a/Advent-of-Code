from aoc import AOC

aoc = AOC(12,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
left =  {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

# Part 1
x, y, d = 0, 0, 'E'
for instruction in input:
    i, v = instruction[0], int(instruction[1:])

    if i == 'N': y += v
    if i == 'S': y -= v
    if i == 'E': x += v
    if i == 'W': x -= v
    if i == 'F':
        if d == 'N': y += v
        if d == 'S': y -= v
        if d == 'E': x += v
        if d == 'W': x -= v
    if i == 'L':
        for j in range(v//90): d = left[d]
    if i == 'R':
        for j in range(v//90): d = right[d]

p1_sol = abs(x) + abs(y)

# Part 2
x, y, d, dx, dy = 0, 0, 'E', 10, 1
for instruction in input:
    i, v = instruction[0], int(instruction[1:])

    if i == 'N': dy += v
    if i == 'S': dy -= v
    if i == 'E': dx += v
    if i == 'W': dx -= v
    if i == 'F':
        x += v*dx
        y += v*dy
    if i == 'L':
        for j in range(v//90):
            dx, dy = -dy, dx
    if i == 'R':
        for j in range(v//90):
            dx, dy = dy, -dx

p2_sol = abs(x) + abs(y)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
