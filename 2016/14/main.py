from aoc import AOC
from hashlib import md5
from functools import cache

aoc = AOC(14,  2016, __file__)

input = 'cuanljph'

@cache
def stream(salt, index, add_iters=0):
    message = salt + str(index)
    for iter in range(add_iters + 1):
        h = md5()
        h.update(message.encode())
        message = h.hexdigest()

    return message

def isKey(salt, index, add_iters=0):
    return any([
        r * 3 in stream(salt, index, add_iters) and
        all([t * 3 not in stream(salt, index, add_iters)[:stream(salt, index, add_iters).index(r * 3)] for t in '0123456789abcdef']) and
        any([r * 5 in stream(salt, index + i, add_iters) for i in range(1, 1_001)])
        for r in '0123456789abcdef'
        ])

index = nb_keys1 = nb_keys2 = 0
index_64th_key1 = index_64th_key2 = None
while index_64th_key1 is None or index_64th_key2 is None:
    if isKey(input, index):
        nb_keys1 += 1
        if nb_keys1 == 64:
            index_64th_key1 = index
    if isKey(input, index, 2016):
        nb_keys2 += 1
        if nb_keys2 == 64:
            index_64th_key2 = index
    index += 1

p1_sol = index_64th_key1
p2_sol = index_64th_key2

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
