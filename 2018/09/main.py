from aoc import AOC
from collections import defaultdict

aoc = AOC(9,  2018, __file__)

input = aoc.input.strip().split('\n')[0].split()

def solve(nb_players, last_marble):
    current_marble = 0
    scores = [0] * nb_players

    next, prev = defaultdict(int), defaultdict(int)
    next[0] = prev[0] = 0

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[(marble - 1) % nb_players] += marble
            for _ in range(7): current_marble = prev[current_marble]
            scores[(marble - 1) % nb_players] += current_marble

            next[prev[current_marble]] = next[current_marble]
            prev[next[current_marble]] = prev[current_marble]

            current_marble = next[current_marble]

        else:
            prev[next[next[current_marble]]] = marble
            next[marble] = next[next[current_marble]]
            next[next[current_marble]] = marble
            prev[marble] = next[current_marble]

            current_marble = marble

    return max(scores)

def part1():
    nb_players, last_marble = int(input[0]), int(input[6])
    return solve(nb_players, last_marble)
 
def part2():
    nb_players, last_marble = int(input[0]), int(input[6])
    return solve(nb_players, last_marble * 100)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
