from aoc import AOC

aoc = AOC(5,  2015, __file__)

input = aoc.input.strip().split('\n')

def nice_1(string):
    nb_vowels = sum([l in 'aeiou' for l in string])
    doubled_letter = any([string[i] == string[i - 1] for i in range(1, len(string))])
    non_forbidden = all([st not in string for st in ['ab', 'cd', 'pq', 'xy']])

    return nb_vowels >= 3 and doubled_letter and non_forbidden

def nice_2(string):
    pair = any([string[i - 2:i] in string[i:] for i in range(2, len(string))])
    repeat = any([string[i] == string[i - 2] for i in range(2, len(string))])

    return pair and repeat

p1_sol = sum([nice_1(string) for string in input])
p2_sol = sum([nice_2(string) for string in input])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
