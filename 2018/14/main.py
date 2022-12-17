from aoc import AOC

aoc = AOC(14,  2018, __file__)

input = 554401
#input = 51589

def part1():
    recipies = [3, 7]
    elves = [0, 1]

    while len(recipies) < input + 10:
        nr = list(map(int, str(sum(recipies[elves[i]] for i in range(2)))))
        recipies += nr

        elves = [(elve + 1 + recipies[elve]) % len(recipies) for elve in elves]

    return ''.join(map(str, recipies[input:input+10]))

def part2():
    target = str(input)
    recipies = '37'
    elves = [0, 1]

    while True:
        nr = str(int(recipies[elves[0]]) + int(recipies[elves[1]]))
        recipies += nr

        elves = [(elve + 1 + int(recipies[elve])) % len(recipies) for elve in elves]

        if recipies[-len(target):] == target:
            return len(recipies) - len(target)
        if recipies[-len(target)-1:-1] == target:
            return len(recipies) - len(target) - 1

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
