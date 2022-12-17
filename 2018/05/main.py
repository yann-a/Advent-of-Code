from aoc import AOC

aoc = AOC(5,  2018, __file__)

input = aoc.input.strip()
# input = aoc.get_example(0).strip().split('\n')

def part1():
    polymer = input
    while True:
        changeHappened = False
        for i in range(len(polymer)-1):
            if polymer[i].lower() == polymer[i+1].lower() and polymer[i].isupper() != polymer[i+1].isupper():
                polymer = polymer[:i] + polymer[i+2:]
                changeHappened = True
                break
        
        if not changeHappened:
            break

    return len(polymer)

def part2():
    minl = 1_000_000_000
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        polymer = ''.join(l for l in input if l.lower() != letter)
        while True:
            changeHappened = False
            for i in range(len(polymer)-1):
                if polymer[i].lower() == polymer[i+1].lower() and polymer[i].isupper() != polymer[i+1].isupper():
                    polymer = polymer[:i] + polymer[i+2:]
                    changeHappened = True
                    break
            
            if not changeHappened:
                break

        minl = min(minl, len(polymer))

    return minl

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)