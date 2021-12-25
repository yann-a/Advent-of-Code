from aoc import AOC

aoc = AOC(16,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

right_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
    }

def part1():
    for i, line in enumerate(input):
        line = ' '.join(line.split()[2:])
        line = line.split(', ')

        sues_things = {}
        for el in line:
            el = el.split(': ')
            sues_things[el[0]] = int(el[1])

        can_be_sue = True
        for el in sues_things:
            if sues_things[el] != right_sue[el]:
                can_be_sue = False
        
        if can_be_sue:
            return i + 1

def part2():
    for i, line in enumerate(input):
        line = ' '.join(line.split()[2:])
        line = line.split(', ')

        sues_things = {}
        for el in line:
            el = el.split(': ')
            sues_things[el[0]] = int(el[1])

        can_be_sue = True
        for el in sues_things:
            if el == 'cats' or el == 'trees':
                if sues_things[el] <= right_sue[el]:
                    can_be_sue = False
            elif el == 'pomeranians' or el == 'goldfish':
                if sues_things[el] >= right_sue[el]:
                    can_be_sue = False
            elif sues_things[el] != right_sue[el]:
                can_be_sue = False
        
        if can_be_sue:
            return i + 1


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
