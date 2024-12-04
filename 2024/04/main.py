from aoc import AOC

aoc = AOC(4,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

h = len(input)
w = len(input[0])

def getInp(y, x):
    if 0 <= y < h and 0 <= x < w:
        return input[y][x]
    else:
        return ''

def part1():
    def isxmas(s):
        return s == 'XMAS' or s == 'SAMX'

    nb = 0
    for y in range(h):
        for x in range(w):
            horiz = getInp(y, x) + getInp(y, x + 1) + getInp(y, x + 2) + getInp(y, x + 3)
            vert = getInp(y, x) + getInp(y + 1, x) + getInp(y + 2, x) + getInp(y + 3, x)
            diag1 = getInp(y, x) + getInp(y + 1, x + 1) + getInp(y + 2, x + 2) + getInp(y + 3, x + 3)
            diag2 = getInp(y, x) + getInp(y - 1, x + 1) + getInp(y - 2, x + 2) + getInp(y - 3, x + 3)

            nb += isxmas(horiz) + isxmas(vert) + isxmas(diag1) + isxmas(diag2)

    return nb

def part2():
    def ismas(s):
        return s == 'MAS' or s == 'SAM'

    nb = 0
    for y in range(h):
        for x in range(w):
            diag1 = getInp(y - 1, x - 1) + getInp(y, x) + getInp(y + 1, x + 1)
            diag2 = getInp(y + 1, x - 1) + getInp(y, x) + getInp(y - 1, x + 1)

            nb += ismas(diag1) * ismas(diag2)

    return nb

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
