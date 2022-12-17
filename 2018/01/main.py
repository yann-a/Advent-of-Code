from aoc import AOC

aoc = AOC(1,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    r = 0
    for line in input:
        r += int(line)

    return r

def part2():
    r = 0
    prev_r = set()
    while True:
        for line in input:
            r += int(line)
            if r in prev_r:
                return r
            else:
                prev_r.add(r)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)