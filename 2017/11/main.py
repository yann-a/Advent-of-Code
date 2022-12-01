from aoc import AOC

aoc = AOC(11,  2017, __file__)

input = aoc.input.strip().split(',')

x = y = 0
max_dist = 0
for inst in input:
    if inst == 'n': y += 1
    if inst == 's': y -= 1
    if inst == 'ne': x, y = x + 1, y + 1 if x % 2 == 0 else y
    if inst == 'se': x, y = x + 1, y if x % 2 == 0 else y - 1
    if inst == 'nw': x, y = x - 1, y + 1 if x % 2 == 0 else y
    if inst == 'sw': x, y = x - 1, y if x % 2 == 0 else y - 1

    dist = (abs(x) + max(abs(y) - abs(x // 2) , 0)) if x % 2 == 0 else (abs(x) + max(abs(y - 0.5) - abs((x + 1) // 2 - 0.5), 0))
    max_dist = max(dist, max_dist)

p1_sol = int(dist)
p2_sol = int(max_dist)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
