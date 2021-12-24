from aoc import AOC

aoc = AOC(22,  2021, __file__)

#input = aoc.get_example(1).strip().split('\n')
input = aoc.input.strip().split('\n')

def getParams(string):
    string = string.split()
    op = string[0]
    c = string[1].split(',')
    c = [list(map(int, l.split('=')[1].split('..'))) for l in c]

    return op, c

def intersection(c, d):
    xm, xM = max(c[0][0], d[0][0]), min(c[0][1], d[0][1])
    ym, yM = max(c[1][0], d[1][0]), min(c[1][1], d[1][1])
    zm, zM = max(c[2][0], d[2][0]), min(c[2][1], d[2][1])

    if xm <= xM and ym <= yM and zm <= zM:
        return [[xm, xM], [ym, yM], [zm, zM]]

offsets = []
for cube in input:
    op, c = getParams(cube)
    offsets_len = len(offsets)

    if op == 'on':
        offsets.append((1, c))
        for op2, c2 in offsets[:offsets_len]:
            inter = intersection(c, c2)
            if inter is not None:
                offsets.append((-op2, inter))
    else:
        for op2, c2 in offsets[:offsets_len]:
            inter = intersection(c, c2)
            if inter is not None:
                offsets.append((-op2, inter))

nb_1 = nb_2 = 0
for (mult, c) in offsets:
    if all([-50 <= c[i][j] <= 50 for i in range(3) for j in range(2)]):
        nb_1 += mult * ((abs(c[0][0] - c[0][1]) + 1) * (abs(c[1][0] - c[1][1]) + 1) * (abs(c[2][0] - c[2][1]) + 1))
    nb_2 += mult * ((abs(c[0][0] - c[0][1]) + 1) * (abs(c[1][0] - c[1][1]) + 1) * (abs(c[2][0] - c[2][1]) + 1))

p1_sol = nb_1
p2_sol = nb_2

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
