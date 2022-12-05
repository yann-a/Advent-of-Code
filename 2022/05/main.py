from aoc import AOC

aoc = AOC(5,  2022, __file__)

input = aoc.input.split('\n\n')
#input = aoc.get_example(0).split('\n\n')

def part1():
    incrates, actions = map(lambda c: c.split('\n'), input)
    crates = [[] for _ in range(len(incrates[-1])//4 + 1)]

    for line in incrates[::-1][1:]:
        for i, c in enumerate(line):
            if c == '[':
                crates[i//4].append(line[i+1])

    for line in actions[:-1]:
        tokens = line.split()
        for _ in range(int(tokens[1])):
            crates[int(tokens[5])-1].append(crates[int(tokens[3])-1].pop(-1))

    return ''.join(crate[-1] for crate in crates)

def part2():
    incrates, actions = map(lambda c: c.split('\n'), input)
    crates = [[] for _ in range(len(incrates[-1])//4 + 1)]

    for line in incrates[::-1][1:]:
        for i, c in enumerate(line):
            if c == '[':
                crates[i//4].append(line[i+1])

    for line in actions[:-1]:
        tokens = line.split()
        for i in range(int(tokens[1])):
            crates[int(tokens[5])-1].append(crates[int(tokens[3])-1].pop(-int(tokens[1])+i))

    return ''.join(crate[-1] for crate in crates)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)