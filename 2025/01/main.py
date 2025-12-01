from aoc import AOC

aoc = AOC(1,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    r = 50
    s = 0
    for inst in input:
        dir, n = inst[0], int(inst[1:])

        if dir == 'L':
            r = (r - n) % 100
        else:
            r = (r + n) % 100

        if r == 0:
            s += 1

    return s

def part2():
    r = 50
    s = 0
    for inst in input:
        dir, n = inst[0], int(inst[1:])

        if dir == 'L':
            s += (r - n) // -100 + (r != 0 or (r - n) % 100 == 0)
            r = (r - n) % 100
        else:
            s += (r + n) // 100
            r = (r + n) % 100

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
