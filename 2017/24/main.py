from aoc import AOC
from collections import defaultdict

aoc = AOC(24,  2017, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def solve1(bridges, d, used, start, cs):
    ncs = cs
    for bridge in d[start]:
        if not used[bridge]:
            u = used[:]
            u[bridge] = True
            ns = bridges[bridge][0] if bridges[bridge][1] == start else bridges[bridge][1]
            ncs = max(ncs, solve1(bridges, d, u, ns, cs + start + ns))

    return ncs

def part1():
    bridges = [list(map(int, bridge.split('/'))) for bridge in input]
    d = defaultdict(list)
    for i in range(len(bridges)):
        d[bridges[i][0]].append(i)
        d[bridges[i][1]].append(i)

    return solve1(bridges, d, [False] * len(bridges), 0, 0)

def solve2(bridges, d, used, start, cl, cs):
    ncs = cs
    nml = cl
    for bridge in d[start]:
        if not used[bridge]:
            u = used[:]
            u[bridge] = True
            ns = bridges[bridge][0] if bridges[bridge][1] == start else bridges[bridge][1]

            l, s = solve2(bridges, d, u, ns, cl + 1, cs + start + ns)
            if l > nml:
                nml = l
                ncs = s
            elif l == nml:
                ncs = max(ncs, s)                

    return nml, ncs

def part2():
    bridges = [list(map(int, bridge.split('/'))) for bridge in input]
    d = defaultdict(list)
    for i in range(len(bridges)):
        d[bridges[i][0]].append(i)
        d[bridges[i][1]].append(i)

    _, s = solve2(bridges, d, [False] * len(bridges), 0, 0, 0)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
