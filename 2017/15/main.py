from aoc import AOC

aoc = AOC(15,  2017, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

a, b = int(input[0].split()[-1]), int(input[1].split()[-1])
A, B, MOD = 16807, 48271, 2147483647

def part1(a, b):
    nb_match = 0
    for i in range(40_000_000):
        a, b = (a * A) % MOD, (b * B) % MOD

        if ('0' * 16 + bin(a)[2:])[-16:] == ('0' * 16 + bin(b)[2:])[-16:]:
            nb_match += 1

    return nb_match

def part2(a, b):
    nb_match = 0
    for i in range(5_000_000):
        a = (a * A) % MOD
        while a % 4 != 0:
            a = (a * A) % MOD

        b = (b * B) % MOD
        while b % 8 != 0:
            b = (b * B) % MOD

        if ('0' * 16 + bin(a)[2:])[-16:] == ('0' * 16 + bin(b)[2:])[-16:]:
            nb_match += 1

    return nb_match

p1_sol = part1(a, b)
p2_sol = part2(a, b)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
