from aoc import AOC

aoc = AOC(5,  2017, __file__)

#input = list(map(int, aoc.get_example(0).strip().split('\n')))
input = list(map(int, aoc.input.strip().split('\n')))

def solve1(offsets):
    pc = steps = 0
    offsets = offsets[:]
    while 0 <= pc < len(offsets):
        steps += 1
        offsets[pc] += 1
        pc += offsets[pc] - 1

    return steps

def solve2(offsets):
    pc = steps = 0
    offsets = offsets[:]
    while 0 <= pc < len(offsets):
        steps += 1

        if offsets[pc] >= 3:
            offsets[pc] -= 1
            pc += offsets[pc] + 1
        else:
            offsets[pc] += 1
            pc += offsets[pc] - 1

    return steps

p1_sol = solve1(input)
p2_sol = solve2(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)