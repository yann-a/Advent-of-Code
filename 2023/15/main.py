from aoc import AOC

aoc = AOC(15,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def hash(word):
    h = 0
    for l in word:
        h += ord(l)
        h *= 17
        h %= 256

    return h

def part1():
    chunks = input[0].split(',')
    return sum(map(hash, chunks))

def part2():
    chunks = input[0].split(',')

    lenses = [([], []) for _ in range(256)]

    for ins in chunks:
        if ins[-1] == '-':
            label = ins[:-1]
            h = hash(label)

            if label in lenses[h][0]:
                i = lenses[h][0].index(label)
                lenses[h][0].pop(i)
                lenses[h][1].pop(i)
        else:
            label = ins[:-2]
            strength = int(ins[-1])
            h = hash(label)

            if label in lenses[h][0]:
                i = lenses[h][0].index(label)
                lenses[h][1][i] = strength
            else:
                lenses[h][0].append(label)
                lenses[h][1].append(strength)

    return sum((i + 1) * sum((j + 1) * lenses[i][1][j] for j in range(len(lenses[i][1]))) for i in range(256))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
