from aoc import AOC

aoc = AOC(1,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    return sum(map(lambda mass: int(mass) // 3 - 2, input))

def part2():
    f = af = 0
    for mass in input:
        af = int(mass) // 3 - 2
        while af > 0:
            f += af
            af = af // 3 - 2

    return f

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
