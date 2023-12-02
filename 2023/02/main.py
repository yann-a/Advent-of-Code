from aoc import AOC

aoc = AOC(2,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1(R, G, B):
    s = 0
    for g_id, line in enumerate(input):
        draws = line.split(': ')[1].split('; ')
        possibleDraw = True

        for draw in draws:
            cubes = draw.split(', ')

            for cube in cubes:
                info = cube.split(' ')
                n = int(info[0])
                c = info[1]

                if (c == 'red' and n > R) or (c == 'green' and n > G) or (c == 'blue' and n > B):
                    possibleDraw = False
                    break

            if not possibleDraw:
                break

        if possibleDraw:
            s += (g_id + 1)

    return s

def part2():
    s = 0
    for g_id, line in enumerate(input):
        draws = line.split(': ')[1].split('; ')
        minr = ming = minb = 0

        for draw in draws:
            cubes = draw.split(', ')

            for cube in cubes:
                info = cube.split(' ')
                n = int(info[0])
                c = info[1]

                if c == 'red': minr = max(minr, n)
                if c == 'green': ming = max(ming, n)
                if c == 'blue': minb = max(minb, n)

        s += minr * ming * minb

    return s

p1_sol = part1(12, 13, 14)
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)