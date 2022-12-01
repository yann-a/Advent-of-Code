from aoc import AOC
from functools import reduce

aoc = AOC(10,  2017, __file__)

input = aoc.input.strip()

def set(list, index, value):
    list[index % len(list)] = value

def get(list, index):
    return list[index % len(list)]

def round(lengths, current=0, skip=0, seq=list(range(256))):
    for l in lengths:
        tmp = [get(seq, current + i) for i in range(l)]
        for i in range(l):
            set(seq, current + i, tmp[len(tmp) - i - 1])
        current += l + skip
        skip += 1

    return seq, current, skip

# Part 1
r = round(list(map(int, input.split(','))))
p1_sol = r[0][0] * r[0][1]

# Part 2
ascii_inp = [ord(c) for c in input]
total_inp = ascii_inp + [17, 31, 73, 47, 23]

current = skip = 0
seq = list(range(256))
for _ in range(64):
    seq, current, skip = round(total_inp, current, skip, seq)

sparse_hash = [reduce(lambda x, y: x ^ y, seq[i * 16 : (i + 1) * 16]) for i in range(16)]
knot_hash = ''.join([('0' + hex(el)[2:])[-2:] for el in sparse_hash])
p2_sol = knot_hash

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
