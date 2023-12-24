from aoc import AOC
from collections import namedtuple
from sympy import Symbol, solve_poly_system

aoc = AOC(24,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

Coords = namedtuple("Coords", ["x", "y", "z"])
Eq = namedtuple("Eq", ["A", "B", "C"])

def part1(boundmin, boundmax):
    position = []
    velocity = []
    equation = []
    for line in input:
        p, v = line.split(' @ ')
        p = Coords(*map(int, p.split(', ')))
        v = Coords(*map(int, v.split(', ')))

        A = v.y
        B = -v.x
        C = A * p.x + B * p.y

        position.append(p)
        velocity.append(v)
        equation.append(Eq(A, B, C)) # Ax + By = C

    inter = 0
    for i in range(len(input)):
        for j in range(i):
            det = equation[i].A * equation[j].B - equation[j].A * equation[i].B

            if det == 0:
                continue
            else:
                x = (equation[j].B * equation[i].C - equation[i].B * equation[j].C) / det
                y = (equation[i].A * equation[j].C - equation[j].A * equation[i].C) / det

                if not (boundmin <= x <= boundmax and boundmin <= y <= boundmax):
                    continue

                ti = (x - position[i].x) / velocity[i].x
                tj = (x - position[j].x) / velocity[j].x

                if ti < 0 or tj < 0:
                    continue

                inter += 1
    return inter

def part2():
    position = []
    velocity = []
    for line in input:
        p, v = line.split(' @ ')
        p = Coords(*map(int, p.split(', ')))
        v = Coords(*map(int, v.split(', ')))

        position.append(p)
        velocity.append(v)

    px = Symbol('px')
    py = Symbol('py')
    pz = Symbol('pz')

    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equations = []
    ts = []

    # 6 unknowns, and each hailstone gives us 3 equations, so 3 hailstones are enough
    for i in range(3):
        t = Symbol(f't{i}')
        ts.append(t)

        equations.append(px + vx * t - position[i].x - velocity[i].x * t)
        equations.append(py + vy * t - position[i].y - velocity[i].y * t)
        equations.append(pz + vz * t - position[i].z - velocity[i].z * t)

    result = solve_poly_system(equations, *([px, py, pz, vx, vy, vz] + ts))

    return result[0][0] + result[0][1] + result[0][2]

#p1_sol = part1(7, 27)
p1_sol = part1(200_000_000_000_000, 40_000_000_000_0000)
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
