from aoc import AOC
from collections import defaultdict

aoc = AOC(4,  2016, __file__)

input = aoc.input.strip().split('\n')

def rotate(string, n):
    str_list = list(string)
    ord_list = list(map(ord, str_list))
    shift_list = list(map(lambda o: (o - ord('a') + n) % 26 + ord('a'), ord_list))
    char_list = list(map(chr, shift_list))

    return ''.join(char_list)

real_ids_sum = 0
north_pole_room = 0
for line in input:
    parts = line.split('-')

    content = ''.join(parts[:-1])
    sector_id = int(parts[-1].split('[')[0])
    checksum = parts[-1].split('[')[1][:-1]

    freqs = defaultdict(int)
    for c in content:
        freqs[c] += 1

    freqs = sorted([(-freqs[c], c) for c in freqs])
    check = ''.join([c for _, c in freqs[:5]])

    if check == checksum:
        real_ids_sum += sector_id

        name = ' '.join([rotate(part, sector_id) for part in parts[:-1]])
        if 'north' in name:
            north_pole_room = sector_id


p1_sol = real_ids_sum
p2_sol = north_pole_room

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
