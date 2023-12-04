from aoc import AOC

aoc = AOC(4,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    s = 0

    for line in input:
        cards = line.split(': ')[1]
        cs = 0

        winning, actual = cards.split(' | ')
        winning = list(map(int, winning.split()))
        actual = list(map(int, actual.split()))

        won = False

        for n in actual:
            if n in winning:
                if won:
                    cs *= 2
                else:
                    cs = 1
                    won = True

        s += cs

    return s

def part2():
    s = 0
    mult = [1 for _ in input]

    for i, line in enumerate(input):
        d = line.split(': ')[1]
        cs = 0

        winning, actual = d.split(' | ')
        winning = list(map(int, winning.split()))
        actual = list(map(int, actual.split()))

        won = False

        for n in actual:
            if n in winning:
                cs += 1

        for j in range(cs):
            if i + 1 + j < len(input):
                mult[i + 1 + j] += mult[i]

    return sum(mult)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)