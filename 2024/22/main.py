from aoc import AOC
from itertools import product
from collections import defaultdict

aoc = AOC(22,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

PFACT = 16777216

def mix(number, a):
    return number ^ a

def prune(number):
    return number % PFACT

def evolve(number):
    number = prune(mix(number, number * 64))
    number = prune(mix(number, number // 32))
    number = prune(mix(number, number * 2048))

    return number

def part1():
    s = 0
    for line in input:
        number = int(line)
        for i in range(2000):
            number = evolve(number)
        
        s += number

    return s

def part2():
    seq_nb = defaultdict(int)
    s = 0
    for line in input:
        number = int(line)
        seen_seqs = set()
        diffs = []
        for i in range(2000):
            nnumber = evolve(number)
            diff = (nnumber % 10) - (number % 10)
            number = nnumber

            diffs.append(diff)

            if len(diffs) >= 4:
                last_four = tuple(diffs[-4:])
                if last_four in seen_seqs:
                    continue
                seen_seqs.add(last_four)
                seq_nb[last_four] += (number % 10)

    return max(seq_nb.values())

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
