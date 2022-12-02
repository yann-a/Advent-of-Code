from aoc import AOC

aoc = AOC(2,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

trad = {'A': 'rock', 'B': 'paper', 'C': 'cisors', 'X': 'rock', 'Y': 'paper', 'Z': 'cisors'}
points = {'rock': 1, 'paper': 2, 'cisors': 3}
win = {'rock': 'cisors', 'paper': 'rock', 'cisors': 'paper'}

def calc_score(adv, pla):
    score = points[pla]

    if win[pla] == adv:
        score += 6
    elif pla == adv:
        score += 3

    return score

def part1():
    score = 0

    for line in input:
        adv, pla = line.split()
        adv, pla = trad[adv], trad[pla]

        score += calc_score(adv, pla)

    return score

def part2():
    score = 0

    for line in input:
        adv, outcome = line.split()
        adv = trad[adv]

        if outcome == 'X':
            pla = win[adv]
        elif outcome == 'Y':
            pla = adv
        else:
            pla = win[win[adv]]

        score += calc_score(adv, pla)

    return score

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)