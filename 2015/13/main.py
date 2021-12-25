from aoc import AOC
from itertools import permutations

aoc = AOC(13,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

hap_rel = {}
guests = set()
for line in input:
    line = line.split()
    guests.add(line[0])
    hap_rel[(line[0], line[-1][:-1])] = int(line[3]) if line[2] == 'gain' else -int(line[3])

def get_max_hap(guests, hap_rel):
    max_hap = 0

    table_set = permutations(guests)
    for p in table_set: 
        hap = 0
        for i in range(len(guests) - 1):
            hap += hap_rel[(p[i], p[i+1])] + hap_rel[(p[i+1], p[i])]
        hap += hap_rel[(p[-1], p[0])] + hap_rel[(p[0], p[-1])]

        max_hap = max(max_hap, hap)
    
    return max_hap

p1_sol = get_max_hap(guests, hap_rel)

for guest in guests:
    hap_rel[(guest, 'Me')] = 0
    hap_rel[('Me', guest)] = 0
guests.add('Me')
p2_sol = get_max_hap(guests, hap_rel)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
