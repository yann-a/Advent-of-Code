from aoc import AOC
from collections import defaultdict
from random import shuffle

aoc = AOC(19,  2015, __file__)

input = aoc.input.strip().split('\n\n')

rules = defaultdict(set)
for line in input[0].split('\n'):
    source, target = line.split(' => ')
    rules[source].add(target)

def apply(molecule):
    molecules = set()
    for i in range(len(molecule)):
        for target in rules[molecule[i]]:
            molecules.add(molecule[:i] + target + molecule[i+1:])
        for target in rules[molecule[i:i+2]]:
            molecules.add(molecule[:i] + target + molecule[i+2:])

    return molecules

def part2(molecule):
    # Relies on randomness, a bit shameful
    medicine = input[1].strip()

    replacements = [(l.split()[-1], l.split()[0]) for l in input[0].split('\n') if '=>' in l]
    replacements.sort(key=lambda x: len(x[0]))
    replacements = replacements[::-1]

    while True:
        shuffle(replacements)

        total = 0
        while True:
            old_medicine = medicine
            for lhs, rhs in replacements:
                if lhs in medicine:
                    medicine = medicine.replace(lhs, rhs, 1)
                    total += 1
                    break
            
            if medicine == 'e':
                return total

            if old_medicine == medicine:
                break


p1_sol = len(apply(input[1]))
p2_sol = part2(input[1])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
