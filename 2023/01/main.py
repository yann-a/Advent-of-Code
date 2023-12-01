from aoc import AOC

aoc = AOC(1,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    s = 0
    for line in input:
        digits = []
        for c in line:
            if '0' <= c <= '9':
                digits.append(int(c))

        s += digits[0] * 10 + digits[-1]

    return s

DNAMES = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part2():
    s = 0
    for line in input:
        digits = []
        for i, c in enumerate(line):
            if '0' <= c <= '9':
                digits.append(int(c))
    
            for id, digit_name in enumerate(DNAMES):
                if i + len(digit_name) <= len(line):
                    if line[i:i+len(digit_name)] == digit_name:
                        digits.append(id + 1)

        s += digits[0] * 10 + digits[-1]

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)