from aoc import AOC

aoc = AOC(25,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def dist(p1, p2):
    return sum(abs(pi1 - pi2) for pi1, pi2 in zip(p1, p2))

def part1():
    constellations = []
    for line in input:
        coords = list(map(int, line.split(',')))

        constellations_in = []
        for constellation_id in range(len(constellations)):
            if any(dist(coords, star) <= 3 for star in constellations[constellation_id]):
                constellations_in.append(constellation_id)

        constellations_in.sort(reverse=True)

        new_const = set([tuple(coords)])
        for constellation_id in constellations_in:
            new_const = new_const.union(constellations[constellation_id])
            constellations.pop(constellation_id)

        constellations.append(new_const)

    return len(constellations)

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
