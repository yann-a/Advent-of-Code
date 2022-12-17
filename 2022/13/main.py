from aoc import AOC
from functools import cmp_to_key

aoc = AOC(13,  2022, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return 1 if p1 < p2 else 0 if p1 == p2 else -1
    elif isinstance(p1, list) and isinstance(p2, int):
        return compare(p1, [p2])
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)
    else:
        for v1, v2 in zip(p1, p2):
            if compare(v1, v2) == 1:
                return 1
            if compare(v1, v2) == -1:
                return -1
        if len(p1) < len(p2):
            return 1
        if len(p2) < len(p1):
            return -1
        return 0

def part1():
    s = 0
    for i, pair in enumerate(input):
        v1, v2 = pair.split('\n')
        a1, a2 = eval(v1), eval(v2)
        
        if compare(a1, a2) == 1:
            s += i + 1

    return s

def part2():
    packets = []
    for pair in input:
        v1, v2 = pair.split('\n')
        a1, a2 = eval(v1), eval(v2)
        packets.append(a1)
        packets.append(a2)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare))
    packets = packets[::-1]

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
