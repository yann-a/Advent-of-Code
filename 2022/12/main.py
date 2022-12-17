from aoc import AOC
from queue import PriorityQueue

aoc = AOC(12,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def height(letter):
    if letter == 'S': return ord('a')
    elif letter == 'E': return ord('z')
    else: return ord(letter)

def reach_E_from(x, y):
    to_visit = PriorityQueue()
    seen = set()
    to_visit.put((0, y, x))

    while not to_visit.empty():
        N, y, x = to_visit.get()

        if (y, x) in seen:
            continue
        seen.add((y, x))

        if input[y][x] == 'E':
            return N

        if y > 0 and height(input[y-1][x]) - height(input[y][x]) < 2:
            to_visit.put((N+1, y-1, x))
        if y < len(input)-1 and height(input[y+1][x]) - height(input[y][x]) < 2:
            to_visit.put((N+1, y+1, x))
        if x > 0 and height(input[y][x-1]) - height(input[y][x]) < 2:
            to_visit.put((N+1, y, x-1))
        if x < len(input[0])-1 and height(input[y][x+1]) - height(input[y][x]) < 2:
            to_visit.put((N+1, y, x+1))

def part1():
    for i in range(len(input)):
        if 'S' in input[i]:
            return reach_E_from(input[i].index('S'), i)

def part2():
    minN = 1_000_000
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'a':
                N = reach_E_from(j, i)
                if N is not None:
                    minN = min(minN, N)

    return minN

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
