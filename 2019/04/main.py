from aoc import AOC

aoc = AOC(4,  2019, __file__)

#input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

min_p = 356261
max_p = 846303

def part1():
    s = 0
    for password in range(min_p, max_p + 1):
        pwd = str(password)
        if any(pwd[i] == pwd[i+1] for i in range(5)) and \
            all(int(pwd[i]) <= int(pwd[i+1]) for i in range(5)):
            s += 1

    return s


def part2():
    s = 0
    for password in range(min_p, max_p + 1):
        pwd = str(password)
        if any(pwd[i] == pwd[i+1] and (i == 0 or pwd[i-1] != pwd[i]) and (i == 4 or pwd[i+2] != pwd[i]) for i in range(5)) and \
            all(int(pwd[i]) <= int(pwd[i+1]) for i in range(5)):
            s += 1

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
