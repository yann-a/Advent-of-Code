from aoc import AOC
from functools import reduce

aoc = AOC(13,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

first_time = int(input[0])
ids = input[1].split(',')

# Part 1
best_id, best_time = int(ids[0]), int(ids[0])*(first_time//int(ids[0]) + 1) - first_time
for id in ids[1:]:
    if id == 'x':
        continue
    
    id = int(id)
    time = id*(first_time//id + 1) - first_time
    if time < best_time:
        best_id, best_time = id, time

p1_sol = best_id * best_time

# Part 2
def euclid(a, b):
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1

    while r2 != 0:
        q = r//r2
        r, u, v, r2, u2, v2 = r2, u2, v2, r - q * r2, u - q * u2, v - q * v2

    return r, u, v

remainders = []
modulos = []
for i, id in enumerate(ids):
    if id == 'x':
        continue

    remainders.append(int(id) - i)
    modulos.append(int(id))

N = reduce(lambda x, y: x * y, modulos)
t = sum([remainders[i] * euclid(modulos[i], N//modulos[i])[2] * (N // modulos[i]) for i in range(len(remainders))])

p2_sol = t % N

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
