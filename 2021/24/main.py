from aoc import AOC

aoc = AOC(24,  2021, __file__)

input = aoc.input.strip().split('\n')

# The 14 blocks of the code, between each call to `inp`, each do
# essentially the same thing. They differ in three places :

# inp w
# mul x 0
# add x z
# mod x 26
# div z (1 | 26)
# add x {COND}
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y {OFFSET}
# mul y x
# add z y

# z if come kind of stack on which we pile / depile elements according to
# the sign of COND, and which has to be empty at the end to succeed

stack = []
corresp = [None] * 14
for i in range(14):
    block = input[18*i:18*(i+1)]
    cond = int(block[5].split()[-1])
    offset = int(block[15].split()[-1])

    if cond >= 0:
        stack.append((i, offset))
    else:
        (j, offset) = stack.pop(-1)
        corresp[i] = offset + cond
        corresp[j] = - offset - cond

p1_sol = p2_sol = ''
for offset in corresp:
    if offset >= 0:
        p1_sol += '9'
        p2_sol += str(1 + offset)
    else:
        p1_sol += str(9 + offset)
        p2_sol += '1'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
