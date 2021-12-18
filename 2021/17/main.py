from aoc import AOC

aoc = AOC(17,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

(xm, xM), (ym, yM) = list(map(lambda x: list(map(int, x[2:].split('..'))), input[0].split(': ')[1].split(', ')))

def shoot(vx, vy):
    x, y = 0, 0
    while x <= xM and y >= ym:
        x, y = x + vx, y + vy
        vx, vy = max(vx - 1, 0), vy - 1

        if xm <= x <= xM and ym <= y <= yM:
            return True
    return False

max_y = abs(ym)*(abs(ym)-1)//2

MINX, MAXX = 1, xM + 1
MINY, MAXY = ym - 1, abs(ym) + 1

nb_in = 0
for vx in range(MINX, MAXX):
    for vy in range(MINY, MAXY):
        if shoot(vx, vy):
            nb_in += 1

p1_sol = max_y
p2_sol = nb_in

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
