from aoc import AOC
from math import lcm

aoc = AOC(8,  2023, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    instructions = input[0].strip()
    graph_ = input[1].split('\n')

    graph = {}

    for line in graph_:
        chunks = line.split()

        origin = chunks[0]
        lr = [chunks[2][1:-1], chunks[3][:-1]]

        graph[origin] = lr

    p = 'AAA'
    s = i = 0
    while p != 'ZZZ':
        p = graph[p][0 if instructions[i] == 'L' else 1]
        s += 1
        i = (i + 1) % len(instructions)

    return s

def part2():
    instructions = input[0].strip()
    graph_ = input[1].split('\n')

    graph = {}

    for line in graph_:
        chunks = line.split()

        origin = chunks[0]
        lr = [chunks[2][1:-1], chunks[3][:-1]]

        graph[origin] = lr

    nodes_ending_in_A = [node for node in graph if node[-1] == 'A']
    r = []

    for node in nodes_ending_in_A:
        p = node
        s = i = 0
        while p[-1] != 'Z':
            p = graph[p][0 if instructions[i] == 'L' else 1]
            s += 1
            i = (i + 1) % len(instructions)

        r.append(s)

    ppcm = lcm(*r)

    return ppcm

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)