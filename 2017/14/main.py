from aoc import AOC
from functools import reduce

aoc = AOC(14,  2017, __file__)

#input = 'flqrgnkx'
input = 'jzgqcdpd'

def set_list(list, index, value):
    list[index % len(list)] = value

def get(list, index):
    return list[index % len(list)]

def round(lengths, current=0, skip=0, seq=list(range(256))):
    for l in lengths:
        tmp = [get(seq, current + i) for i in range(l)]
        for i in range(l):
            set_list(seq, current + i, tmp[len(tmp) - i - 1])
        current += l + skip
        skip += 1

    return seq, current, skip

def knot_hash(string):
    hash_input = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    current = skip = 0
    seq = list(range(256))
    for _ in range(64):
        seq, current, skip = round(hash_input, current, skip, seq)

    sparse_hash = [reduce(lambda x, y: x ^ y, seq[i * 16 : (i + 1) * 16]) for i in range(16)]
    return ''.join([('0' + hex(el)[2:])[-2:] for el in sparse_hash])

grid = []
for i in range(128):
    grid.append(knot_hash(input + '-' + str(i)))

def browse(x, y, seen):
    if (x, y) in seen:
        return 0
    seen.add((x, y))

    nb_browsed = 1
    for d in [-1, 1]:
        if 0 <= x + d < 128 and ('0' * 128 + bin(int(grid[y], 16))[2:])[-128:][x + d] == '1':
            nb_browsed += browse(x + d, y , seen)
        if 0 <= y + d < 128 and ('0' * 128 + bin(int(grid[y + d], 16))[2:])[-128:][x] == '1':
            nb_browsed += browse(x, y + d, seen)

    return nb_browsed

nb_groups = nb_squares = 0
seen = set()
for x in range(128):
    for y in range(128):
        if ('0' * 128 + bin(int(grid[y], 16))[2:])[-128:][x] == '1' and (x, y) not in seen:
            nb_groups += 1
            nb_squares += browse(x, y, seen)

p1_sol = nb_squares
p2_sol = nb_groups

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
