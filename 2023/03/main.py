from aoc import AOC
from collections import defaultdict

aoc = AOC(3,  2023, __file__)

input = aoc.input.strip().split('\n')
input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0
    for line in range(len(input)):
        for row in range(len(input[0])):
            if '0' <= input[line][row] <= '9' and (row == 0 or (not ('0' <= input[line][row - 1] <= '9'))):
                
                pt = row
                while pt < len(input[0]) and '0' <= input[line][pt] <= '9':
                    pt += 1

                n = int(input[line][row:pt])

                isAdj = False

                for dline in range(line - 1, line + 2):
                    for drow in range(row - 1, pt + 1):
                        if 0 <= dline < len(input) and 0 <= drow < len(input[0]) and (not (dline == line and row <= drow < pt)):
                            if input[dline][drow] != '.':
                                isAdj = True

                if isAdj:
                    s += n
    return s

def part2():
    gears = defaultdict(list)
    for line in range(len(input)):
        for row in range(len(input[0])):
            if '0' <= input[line][row] <= '9' and (row == 0 or (not ('0' <= input[line][row - 1] <= '9'))):
                pt = row
                while pt < len(input[0]) and '0' <= input[line][pt] <= '9':
                    pt += 1

                n = int(input[line][row:pt])

                for dline in range(line - 1, line + 2):
                    for drow in range(row - 1, pt + 1):
                        if 0 <= dline < len(input) and 0 <= drow < len(input[0]) and (not (dline == line and row <= drow < pt)):
                            if input[dline][drow] == '*':
                                gears[(dline, drow)].append(n)
    
    s = 0
    for key in gears:
        if len(gears[key]) == 2:
            s += gears[key][0] * gears[key][1]

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)