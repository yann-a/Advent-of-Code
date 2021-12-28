from aoc import AOC

aoc = AOC(19,  2016, __file__)

input = 3001330

def part1(nb_elves):
    next_elves = {e + 1: (e + 1) % nb_elves + 1 for e in range(nb_elves)}
    turn = 1
    for _ in range(nb_elves):
        next_elve = next_elves[turn]
        next_next_elve = next_elves[next_elve]
        
        next_elves[turn] = next_next_elve
        turn = next_next_elve

    return turn

def part2_long(nb_elves):
    # next, prev, target
    elves = {e + 1 : [(e + 1) % nb_elves + 1, (e - 1) % nb_elves + 1, (e + nb_elves // 2) % nb_elves + 1] for e in range(nb_elves)}
    turn = 1
    for N in range(nb_elves):
        killed_elve = elves[turn][2]

        if (nb_elves - N) % 2 == 1:
            i = turn
            while i != killed_elve:
                elves[i][2] = elves[elves[i][2]][0]
                i = elves[i][0]
        else:
            i = killed_elve
            while i != turn:
                i = elves[i][0]
                elves[i][2] = elves[elves[i][2]][1]

        elves[elves[killed_elve][1]][0] = elves[killed_elve][0]
        elves[elves[killed_elve][0]][1] = elves[killed_elve][1]
        turn = elves[turn][0]

    return turn

#for nb_elves in range(1, 100):
#    print(f'{nb_elves}: {part2_long(nb_elves)}')

# Hacky solution : by looking at the outputs for numbers of elves from 1 to 100, we deduce the pattern
def part2(nb_elves):
    i = 0
    n = 0
    previous_max = 1
    while n < nb_elves:
        for j in range(1, previous_max):
            n += 1
            if n == nb_elves:
                return j
        for j in range(previous_max, 3 ** i + 1, 2):
            n += 1
            if n == nb_elves:
                return j
        previous_max = j
        i += 1

p1_sol = part1(input)
p2_sol = part2(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
