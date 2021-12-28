from aoc import AOC

aoc = AOC(2,  2016, __file__)

input = aoc.input.strip().split('\n')

def part1():
    code = ''
    x = y = 1
    for line in input:
        for move in line:
            if move == 'U':
                y = max(0, y - 1)
            elif move == 'R':
                x = min(2, x + 1)
            elif move == 'D':
                y = min(2, y + 1)
            elif move == 'L':
                x = max(0, x - 1)

        code += str(3 * y + x + 1)
    
    return code

def part2():
    KEYPAD = '##1###234#56789#ABC###D##'
    code = ''
    x = y = 2
    for line in input:
        for move in line:
            if move == 'U':
                y = max(abs(2 - x), y - 1)
            elif move == 'R':
                x = min(4 - abs(2 - y), x + 1)
            elif move == 'D':
                y = min(4 - abs(2 - x), y + 1)
            elif move == 'L':
                x = max(abs(2 - y), x - 1)

        code += KEYPAD[5 * y + x]
    
    return code

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
