from aoc import AOC
import numpy as np

aoc = AOC(13,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0
    for machine in input:
        mp = 1000000

        machine = machine.split('\n')
        bax, bay = map(int, machine[0][12:].split(', Y+'))
        bbx, bby = map(int, machine[1][12:].split(', Y+'))
        tx, ty = map(int, machine[2][9:].split(', Y='))

        for va in range(101):
            for vb in range(101):
                if va * bax + vb * bbx == tx and va * bay + vb * bby == ty:
                    mp = min(mp, va * 3 + vb)

        if mp < 1000000:
            s += mp

    return s

def part2():
    s = 0
    for machine in input:
        mp = 1000000

        machine = machine.split('\n')
        bax, bay = map(int, machine[0][12:].split(', Y+'))
        bbx, bby = map(int, machine[1][12:].split(', Y+'))
        tx, ty = map(int, machine[2][9:].split(', Y='))

        m = np.array([
            [bax, bbx],
            [bay, bby]
        ])
        b = np.array([[tx + 10000000000000], [ty + 10000000000000]])

        sol = np.linalg.solve(m, b)
        va, vb = sol[0][0], sol[1][0]

        if abs(round(va) - va) < 0.0001 and abs(round(vb) - vb) < 0.0001 and round(va) >= 0 and round(vb) >= 0:
            s += 3 * round(va) + round(vb)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
