from aoc import AOC
from collections import defaultdict
from functools import cache
from queue import PriorityQueue
import sys

aoc = AOC(20,  2018, __file__)
sys.setrecursionlimit(10_000)

input = aoc.input.strip().split('\n')[0][1:-1]
#input = '^ENWWW(NEEE|SSE(EE|N))$'[1:-1]
#input = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'[1:-1]
#input = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'[1:-1]

dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': 1, 'E': 0, 'S': -1, 'W': 0}

def outer_explore_option(x, y, i, parenthesis, splits, doors):
    @cache
    def explore_option(x, y, i, next):
        ox, oy = x, y
        while i < len(input) and input[i] not in '(|)':
            l = input[i]
            doors.add((x + dx[l], y + dy[l]))
            x, y = x + 2 * dx[l], y + 2 * dy[l]
            i += 1

        if i >= len(input): return

        if input[i] == '(':
            sp = [i] + splits[i]
            for k in range(len(sp)):
                explore_option(x, y, sp[k] + 1, tuple(list(next) + [parenthesis[i] + 1]))
        elif input[i] == ')': explore_option(x, y, next[-1], tuple(list(next)[:-1]))

    explore_option(x, y, i, tuple([]))

def browse(doors):
    mind = {}

    q = PriorityQueue()
    seen = set()

    q.put((0, 0, 0))
    while not q.empty():
        d, x, y = q.get()
        if (x, y) in seen: continue

        seen.add((x, y))
        mind[(x, y)] = d

        for direction in 'NESW':
            if (x + dx[direction], y + dy[direction]) in doors:
                q.put((d + 1, x + 2 * dx[direction], y + 2 * dy[direction]))

    return mind

def print_grid():
    for j in range(10, -11, -1):
        for i in range(-10, 11):
            if i == 0 and j == 0: print('X', end='')
            elif i % 2 == 0 and j % 2 == 0: print('.', end='')
            elif i % 2 == 0 and j % 2 == 1: print('-' if (i, j) in doors else '#', end='')
            elif i % 2 == 1 and j % 2 == 0: print('|' if (i, j) in doors else '#', end='')
            elif i % 2 == 1 and j % 2 == 1: print('#', end='')
        print()

def solve():
    parenthesis = {}
    splits = defaultdict(list)
    stack = [0]
    for i in range(len(input)):
        if input[i] == '(': stack.append(i)
        elif input[i] == ')': parenthesis[stack.pop(-1)] = i
        elif input[i] == '|': splits[stack[-1]].append(i)

    doors = set()
    outer_explore_option(0, 0, 0, parenthesis, splits, doors)
    mind = browse(doors)

    return max(mind.values()), sum(mind[p] >= 1_000 for p in mind)

p1_sol, p2_sol = solve()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
