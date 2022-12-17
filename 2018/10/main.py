from aoc import AOC

aoc = AOC(10,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

def part2():
    points = []
    for line in input:
        line = line[10:-1].split('> velocity=<')
        points.append([tuple(map(int, line[0].split(', '))), tuple(map(int, line[1].split(', ')))])

    seconds = 0
    while True:
        pos = set(p[0] for p in points)
        minx = min(p[0] for p in pos)
        maxx = max(p[0] for p in pos)
        miny = min(p[1] for p in pos)
        maxy = max(p[1] for p in pos)

        if abs(maxy - miny) <= 10:
            for y in range(miny, maxy + 1):
                for x in range(minx, maxx + 1):
                    if (x, y) in pos: print('#', end='')
                    else: print(' ', end='')
                print()
            break

        for i in range(len(points)):
            points[i][0] = (points[i][0][0] + points[i][1][0], points[i][0][1] + points[i][1][1])
        seconds += 1

    return seconds

p2_sol = part2()
p1_sol = 'PHFZCEZX'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
