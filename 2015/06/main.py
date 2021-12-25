from aoc import AOC

aoc = AOC(6,  2015, __file__)

input = aoc.input.strip().split('\n')

def part1(instructions):
    lights = [[False for _ in range(1_000)] for _ in range(1_000)]

    for instruction in instructions:
        if instruction[1] == 'o':
            inst = 'toggle'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[7:].split(' through '))
        elif instruction[6] == 'n':
            inst = 'on'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[8:].split(' through '))
        else:
            inst = 'off'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[9:].split(' through '))
        


        for x in range(xm, xM + 1):
            for y in range(ym, yM + 1):
                lights[x][y] = True if inst == 'on' else False if inst == 'off' else not lights[x][y]

    return sum([sum(l) for l in lights])

def part2(instructions):
    lights = [[0 for _ in range(1_000)] for _ in range(1_000)]

    for instruction in instructions:
        if instruction[1] == 'o':
            inst = 'toggle'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[7:].split(' through '))
        elif instruction[6] == 'n':
            inst = 'on'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[8:].split(' through '))
        else:
            inst = 'off'
            (xm, ym), (xM, yM) = map(lambda p: map(int, p.split(',')), instruction[9:].split(' through '))
        


        for x in range(xm, xM + 1):
            for y in range(ym, yM + 1):
                lights[x][y] = lights[x][y] + 1 if inst == 'on' else max(0, lights[x][y] - 1) if inst == 'off' else lights[x][y] + 2

    return sum([sum(l) for l in lights])

p1_sol = part1(input)
p2_sol = part2(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
