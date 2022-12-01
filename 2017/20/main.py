from aoc import AOC
from collections import defaultdict

aoc = AOC(20,  2017, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

# vn = v(n-1) + a                                       = v0 + n * a
# pn = p(n-1) + v(n-1)  = p0 + \sum_{i=0}^{n-1} v(i)    = p0 + n * v0 + a * n * (n-1) / 2

def part1():
    min_s, s = 1_000_000, 0
    for i, line in enumerate(input):
        p, v, a = line.split(', ')

        if sum(map(lambda t: abs(int(t)), a[3:-1].split(','))) < min_s:
            min_s = sum(map(lambda t: abs(int(t)), a[3:-1].split(',')))
            s = i

    return s

def part2():
    particles = defaultdict(list)
    for line in input:
        p, v, a = line.split(', ')
        P = tuple(map(int, p[3:-1].split(',')))
        V = tuple(map(int, v[3:-1].split(',')))
        A = tuple(map(int, a[3:-1].split(',')))
        particles[P].append((P, V, A))

    for _ in range(100):
        new_particles = defaultdict(list)
        for p in particles:
            if len(particles[p]) == 1:
                p, v, a = particles[p][0]
                v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
                p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
                new_particles[p].append((p, v, a))

        particles = new_particles

    return len(particles)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)

# p + n * v + a * n * (n-1) / 2 = P + n * V + A * n * (n-1)/2
# p + n * v + a / 2 * (n^2 - n) = P + n * V + A / 2 * (n^2 - n)
# (a/2 - A/2) * n^2 + (v - V + A/2 - a/2) * n + p - P = 0
# D = ((v - V) - (a - A)/2)^2 - 4 * (a - A)/2 * (p - P)
#   = (v - V)^2 - (v - V) * (a - A) + (a - A)^2/4 - 2 * (a - A) * (p - P)
# 
# x1 = 