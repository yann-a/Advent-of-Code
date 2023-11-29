from aoc import AOC
from math import lcm

aoc = AOC(12,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    moons = []
    for line in input:
        line = line[1:-1].split(', ')
        moons.append([[int(line[0][2:]), int(line[1][2:]), int(line[2][2:])], [0, 0, 0]])

    for _ in range(1_000):
        for m1 in range(len(moons)):
            for m2 in range(m1):
                for d in range(3):
                    if moons[m1][0][d] < moons[m2][0][d]:
                        moons[m1][1][d] += 1
                        moons[m2][1][d] -= 1
                    elif moons[m1][0][d] > moons[m2][0][d]:
                        moons[m1][1][d] -= 1
                        moons[m2][1][d] += 1

        for moon in range(len(moons)):
            for d in range(3):
                moons[moon][0][d] += moons[moon][1][d]

    total_energy = sum(sum(abs(moons[moon][0][d]) for d in range(3)) * sum(abs(moons[moon][1][d]) for d in range(3)) for moon in range(len(moons)))
    return total_energy

def part2():
    moons = []
    for line in input:
        line = line[1:-1].split(', ')
        moons.append([[int(line[0][2:]), int(line[1][2:]), int(line[2][2:])], [0, 0, 0]])

    hist = [set() for _ in range(3)]
    while True:
        for m1 in range(len(moons)):
            for m2 in range(m1):
                for d in range(3):
                    if moons[m1][0][d] < moons[m2][0][d]:
                        moons[m1][1][d] += 1
                        moons[m2][1][d] -= 1
                    elif moons[m1][0][d] > moons[m2][0][d]:
                        moons[m1][1][d] -= 1
                        moons[m2][1][d] += 1

        for moon in range(len(moons)):
            for d in range(3):
                moons[moon][0][d] += moons[moon][1][d]

        pos = [tuple((moons[moon][0][d], moons[moon][1][d]) for moon in range(len(moons))) for d in range(3)]

        if all(pos[d] in hist[d] for d in range(3)): return lcm(len(hist[0]), len(hist[1]), len(hist[2]))

        for d in range(3): hist[d].add(pos[d])
    
p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
