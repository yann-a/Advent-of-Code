from aoc import AOC

aoc = AOC(16,  2016, __file__)

input = '01111010110010011'

def expand(data):
    a = b = data
    b = b[::-1]
    b = ''.join(['0' if c == '1' else '1' for c in b])

    return a + '0' + b

def solve(data, disk_size):
    while len(data) < disk_size:
        data = expand(data)

    checksum = data[:disk_size]
    while len(checksum) % 2 == 0:
        checksum = ''.join([str(int(checksum[i] == checksum[i+1])) for i in range(0, len(checksum), 2)])

    return checksum

p1_sol = solve(input, 272)
p2_sol = solve(input, 35651584)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)

