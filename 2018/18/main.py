from aoc import AOC
from collections import defaultdict

aoc = AOC(18,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

def part1():
    map = [list(line) for line in input]
    for _ in range(10):
        old_map = [line[:] for line in map]
        for i in range(len(map)):
            for j in range(len(map[i])):
                count = defaultdict(int)
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if (di != 0 or dj != 0) and 0 <= i + di < len(map) and 0 <= j + dj < len(map[i+di]):
                            count[old_map[i+di][j+dj]] += 1

                if old_map[i][j] == '.': map[i][j] = '|' if count['|'] >= 3 else '.'
                elif old_map[i][j] == '|': map[i][j] = '#' if count['#'] >= 3 else '|'
                else: map[i][j] = '#' if count['#'] >= 1 and count['|'] >= 1 else '.'

    trees = sum(sum(map[i][j] == '|' for j in range(len(map[i]))) for i in range(len(map)))
    lumberyards = sum(sum(map[i][j] == '#' for j in range(len(map[i]))) for i in range(len(map)))

    return trees * lumberyards


def part2():
    map = [list(line) for line in input]
    states = {}
    rounds = 0
    while True:
        current_printout = ''.join(''.join(line) for line in map)
        if current_printout in states:
            break
        else:
            states[current_printout] = rounds

        old_map = [line[:] for line in map]
        for i in range(len(map)):
            for j in range(len(map[i])):
                count = defaultdict(int)
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if (di != 0 or dj != 0) and 0 <= i + di < len(map) and 0 <= j + dj < len(map[i+di]):
                            count[old_map[i+di][j+dj]] += 1

                if old_map[i][j] == '.': map[i][j] = '|' if count['|'] >= 3 else '.'
                elif old_map[i][j] == '|': map[i][j] = '#' if count['#'] >= 3 else '|'
                else: map[i][j] = '#' if count['#'] >= 1 and count['|'] >= 1 else '.'

        rounds += 1

    first_occurence = states[current_printout]
    second_occurence = rounds
    
    delta = second_occurence - first_occurence

    map = [list(current_printout[50*i:50*(i+1)]) for i in range(50)]
    for _ in range((1_000_000_000 - first_occurence) % delta):
        old_map = [line[:] for line in map]
        for i in range(len(map)):
            for j in range(len(map[i])):
                count = defaultdict(int)
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if (di != 0 or dj != 0) and 0 <= i + di < len(map) and 0 <= j + dj < len(map[i+di]):
                            count[old_map[i+di][j+dj]] += 1

                if old_map[i][j] == '.': map[i][j] = '|' if count['|'] >= 3 else '.'
                elif old_map[i][j] == '|': map[i][j] = '#' if count['#'] >= 3 else '|'
                else: map[i][j] = '#' if count['#'] >= 1 and count['|'] >= 1 else '.'

    trees = sum(sum(map[i][j] == '|' for j in range(len(map[i]))) for i in range(len(map)))
    lumberyards = sum(sum(map[i][j] == '#' for j in range(len(map[i]))) for i in range(len(map)))

    return trees * lumberyards

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
