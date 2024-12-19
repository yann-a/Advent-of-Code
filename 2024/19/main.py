from aoc import AOC
from collections import defaultdict
from functools import cache

aoc = AOC(19,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    available, goals = input
    available = available.split(', ')
    
    available_d = defaultdict(set)
    for a in available:
        available_d[a[0]].add(a)

    @cache
    def match(goal, i):
        if i == len(goal):
            return True

        for a in available_d[goal[i]]:
            if i + len(a) <= len(goal) and goal[i:i+len(a)] == a:
                if match(goal, i + len(a)):
                    return True

        return False

    s = 0
    for goal in goals.split('\n'):
        s += match(goal, 0)

    return s

def part2():
    available, goals = input
    available = available.split(', ')
    
    available_d = defaultdict(set)
    for a in available:
        available_d[a[0]].add(a)

    @cache
    def match(goal, i):
        if i == len(goal):
            return 1

        ways = 0
        for a in available_d[goal[i]]:
            if i + len(a) <= len(goal) and goal[i:i+len(a)] == a:
                ways += match(goal, i + len(a))

        return ways

    s = 0
    for goal in goals.split('\n'):
        s += match(goal, 0)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
