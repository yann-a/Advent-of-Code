from aoc import AOC
from intcode import *

aoc = AOC(17,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)
    intcode.run()

    scaffoldings = ''
    while len(intcode.output) > 0:
        scaffoldings += chr(intcode.getOutput())
    scaffoldings = scaffoldings.strip().split('\n')

    #sy = [i for i in range(len(scaffoldings)) if any(robot in scaffoldings[i] for robot in '^>v<')][0]
    #sx = [scaffoldings[sy].index(robot) for robot in '^>v<' if robot in scaffoldings[sy]][0]

    return sum(x*y for y in range(1, len(scaffoldings)-1) for x in range(1, len(scaffoldings[0])-1) if sum(scaffoldings[y+dy][x+dx] == '#' for dy in range(-1, 2) for dx in range(-1, 2) if abs(dx) + abs(dy) <= 1)
     == 5)

def get_fullpath():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)
    intcode.run()

    scaffoldings = ''
    while len(intcode.output) > 0:
        scaffoldings += chr(intcode.getOutput())
    scaffoldings = scaffoldings.strip().split('\n')

    y = [i for i in range(len(scaffoldings)) if any(robot in scaffoldings[i] for robot in '^>v<')][0]
    x = [scaffoldings[y].index(robot) for robot in '^>v<' if robot in scaffoldings[y]][0]
    d = '^>v<'.index(scaffoldings[y][x])
    path = []
    while True:
        while True:
            nx = x + (d == 1) - (d == 3)
            ny = y + (d == 2) - (d == 0)

            if 0 <= ny < len(scaffoldings) and 0 <= nx < len(scaffoldings[0]) and scaffoldings[ny][nx] == '#':
                if isinstance(path[-1], int): path[-1] += 1
                else: path.append(1)
                x, y = nx, ny
            else:
                break

        for nd in range(4):
            if nd == (d + 2) % 4: continue

            nx = x + (nd == 1) - (nd == 3)
            ny = y + (nd == 2) - (nd == 0)

            if 0 <= ny < len(scaffoldings) and 0 <= nx < len(scaffoldings[0]) and scaffoldings[ny][nx] == '#':
                if nd == (d + 1) % 4: path.append('R')
                else: path.append('L')

                d = nd
                break
        else:
            break

    return ','.join(map(str, path))

def part2():
    program = list(map(int, input[0].split(',')))
    program[0] = 2
    intcode = IntCodeProgram(program)

    # computed by hand using the result of get_fullpath
    patterns = ['A,A,B,C,B,C,B,C,C,A', 'R,8,L,4,R,4,R,10,R,8', 'L,12,L,12,R,8,R,8', 'R,10,R,4,R,4']
    for char in '\n'.join(patterns) + '\nn\n':
        intcode.addInput(ord(char))

    intcode.run()
    return intcode.output[-1]

p1_sol = part1()
print(get_fullpath())
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
