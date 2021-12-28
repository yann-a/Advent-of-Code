from aoc import AOC

aoc = AOC(1,  2016, __file__)

input = aoc.input.strip().split(', ')

TURNS = {
    'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
    'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
}

dir = 'N'
x = y = 0
vx = vy = None
visited = set([(0, 0)])
for instruction in input:
    dir = TURNS[instruction[0]][dir]

    for i in range(int(instruction[1:])):
        x += (dir == 'E') - (dir == 'W')
        y += (dir == 'N') - (dir == 'S')

        if vx is None and (x, y) in visited:
            vx, vy = x, y

        visited.add((x, y))

p1_sol = abs(x) + abs(y)
p2_sol = abs(vx) + abs(vy)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
