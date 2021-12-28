from aoc import AOC
from functools import reduce

aoc = AOC(15,  2016, __file__)

input = aoc.input.strip().split('\n')

def euclid(a, b):
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1

    while r2 != 0:
        q = r//r2
        r, u, v, r2, u2, v2 = r2, u2, v2, r - q * r2, u - q * u2, v - q * v2

    return r, u, v

remainders = []
modulos = []
for k, line in enumerate(input):
    line = line.split()
    
    nb_pos = int(line[3])
    init_pos = int(line[-1][:-1])

    remainders.append((-init_pos - k - 1) % nb_pos)
    modulos.append(nb_pos)

def solve(remainders, modulos):
    N = reduce(lambda x, y: x * y, modulos)
    t = sum([remainders[i] * euclid(modulos[i], N//modulos[i])[2] * (N // modulos[i]) for i in range(len(remainders))]) % N

    return t

p1_sol = solve(remainders, modulos)

remainders.append((-7) % 11)
modulos.append(11)
p2_sol = solve(remainders, modulos)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
