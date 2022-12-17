from aoc import AOC
from queue import PriorityQueue

aoc = AOC(15,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = open('example6', 'r').read().strip().split('\n')

def search(map, available_spots, i, j):
    q = PriorityQueue()
    q.put((0, i, j, i, j))

    seen = set()

    while not q.empty():
        distance, ni, nj, fi, fj = q.get()

        if (ni, nj) in seen:
            continue

        seen.add((ni, nj))
        for d in [-1, 1]:
            if map[ni+d][nj] == '.': q.put((distance+1, ni+d, nj, fi if distance > 0 else ni + d, fj))
            elif map[ni+d][nj] in 'EG' and map[ni+d][nj] != map[i][j]: available_spots.append((distance, ni, nj, fi, fj))

            if map[ni][nj+d] == '.': q.put((distance+1, ni, nj+d, fi, fj if distance > 0 else nj + d))
            elif map[ni][nj+d] in 'EG' and map[ni][nj+d] != map[i][j]: available_spots.append((distance, ni, nj, fi, fj))
    
def fight(elves_power=3):
    map = [list(line) for line in input]
    units = {}
    nb_units = {'G': 0, 'E': 0}
    for i in range(len(map)):
        for j in range(len(map[i])):
            map_el = map[i][j]
            if map_el in 'EG':
                units[(i, j)] = (map_el, 200)
                nb_units[map_el] += 1

    full_rounds = 0
    while True:
        units_l = sorted(units.keys())
        killed = set()

        for (i, j) in units_l:
            if (i, j) in killed:
                continue

            if any(nb_units[k] == 0 for k in nb_units):
                return full_rounds * sum(units[k][1] for k in units)

            type, hit_points = units[(i, j)]

            # Move
            available_spots = []
            search(map, available_spots, i, j)

            available_spots.sort()

            if len(available_spots) != 0:
                selected = available_spots[0]

                del units[(i, j)]
                map[i][j] = '.'
                i, j = selected[3], selected[4]
                units[(i, j)] = (type, hit_points)
                map[i][j] = type

            # Attack 
            fhp = 201
            if map[i-1][j] in nb_units and units[(i-1,j)][0] != type and units[(i-1, j)][1] < fhp: ai, aj, fhp = i-1, j, units[(i-1, j)][1]
            if map[i][j-1] in nb_units and units[(i,j-1)][0] != type and units[(i, j-1)][1] < fhp: ai, aj, fhp = i, j-1, units[(i, j-1)][1]
            if map[i][j+1] in nb_units and units[(i,j+1)][0] != type and units[(i, j+1)][1] < fhp: ai, aj, fhp = i, j+1, units[(i, j+1)][1]
            if map[i+1][j] in nb_units and units[(i+1,j)][0] != type and units[(i+1, j)][1] < fhp: ai, aj, fhp = i+1, j, units[(i+1, j)][1]
            
            if fhp == 201:
                continue

            atype, ahp = units[(ai, aj)]
            ahp -= (3 if type == 'G' else elves_power)

            if ahp <= 0:
                nb_units[atype] -= 1
                del units[(ai, aj)]
                map[ai][aj] = '.'
                killed.add((ai, aj))

                if atype == 'E' and elves_power > 3:
                    return None
            else:
                units[(ai, aj)] = (atype, ahp)

        full_rounds += 1

def part1():
    return fight()

def part2():
    elves_power = 4
    while True:
        res = fight(elves_power)
        if res is not None:
            return res
        elves_power += 1

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#.submit(2, p2_sol)
