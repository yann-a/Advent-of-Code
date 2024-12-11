from aoc import AOC
from functools import cache

aoc = AOC(11,  2024, __file__)

input = list(map(int, aoc.input.strip().split('\n')[0].split()))
#input = [125, 17]

def apply(l):
    i = 0
    while i < len(l):
        if l[i] == 0:
            l[i] = 1
            i += 1
        elif len(str(l[i])) % 2 == 0:
            n = len(str(l[i]))
            a, b = str(l[i])[:n//2], str(l[i])[n//2:]

            l[i] = int(a)
            l.insert(i + 1, int(b))

            i += 2
        else:
            l[i] *= 2024

            i += 1

@cache
def applysmart(v, n):
    if n == 75:
        return 1
    elif v == 0:
        return applysmart(1, n + 1)
    elif len(str(v)) % 2 == 0:
        nb = len(str(v))
        a, b = str(v)[:nb//2], str(v)[nb//2:]
        return applysmart(int(a), n + 1) + applysmart(int(b), n + 1)
    else:
        return applysmart(v * 2024, n + 1)

def part1():
    data = input[:]
    for _ in range(25):
        apply(data)

    return len(data)

def part2():
    data = input[:]
    s = 0
    for v in data:
        s += applysmart(v, 0)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
