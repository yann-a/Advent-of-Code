from aoc import AOC
from collections import defaultdict

aoc = AOC(3,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

def part1():
    p1 = input[0].split(',')
    p2 = input[1].split(',')

    mind = 1_000_000_000

    p1_path = set()
    x, y = 0, 0
    for op in p1:
        d = op[0]
        for l in range(int(op[1:])):
            x = x + (d == 'R') - (d == 'L')
            y = y + (d == 'U') - (d == 'D')
            p1_path.add((x, y))
    
    x, y = 0, 0
    for op in p2:
        d = op[0]
        for l in range(int(op[1:])):
            x = x + (d == 'R') - (d == 'L')
            y = y + (d == 'U') - (d == 'D')
            
            if (x, y) in p1_path:
                mind = min(mind, abs(x) + abs(y))

    return mind

def part2():
    p1 = input[0].split(',')
    p2 = input[1].split(',')

    mins = 1_000_000_000

    p1_path = defaultdict(lambda: 1_000_000_000)
    x, y, s = 0, 0, 0
    for op in p1:
        d = op[0]
        for l in range(int(op[1:])):
            x = x + (d == 'R') - (d == 'L')
            y = y + (d == 'U') - (d == 'D')
            s += 1

            p1_path[(x, y)] = min(p1_path[(x, y)], s)
    
    x, y, s = 0, 0, 0
    for op in p2:
        d = op[0]
        for l in range(int(op[1:])):
            x = x + (d == 'R') - (d == 'L')
            y = y + (d == 'U') - (d == 'D')
            s += 1
            
            if (x, y) in p1_path:
                mins = min(mins, p1_path[(x, y)] + s)

    return mins

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
