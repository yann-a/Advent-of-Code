from aoc import AOC

aoc = AOC(6,  2022, __file__)

input = aoc.input.split('\n')[0]
#input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

def part1():
    for i in range(len(input)-4):
        if len(set(input[i:i+4])) == 4:
            return i + 4

def part2():
    for i in range(len(input)-14):
        if len(set(input[i:i+14])) == 14:
            return i + 14

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
