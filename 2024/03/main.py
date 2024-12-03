from aoc import AOC
import re

aoc = AOC(3,  2024, __file__)

input = aoc.input.strip()
#input = aoc.get_example(1).strip()

def part1():
    s = 0
    for match in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input):
        s += int(match[0]) * int(match[1])

    return s

def part2():
    s = 0
    enabled = True
    for match in re.finditer(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', input):
        if match.group(0) == 'do()':
            enabled = True
        elif match.group(0) == 'don\'t()':
            enabled = False
        elif enabled:
            s += int(match.group(2)) * int(match.group(3))

    return s


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
