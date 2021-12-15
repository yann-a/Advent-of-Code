from aoc import AOC
import sys
sys.setrecursionlimit(100_000)

aoc = AOC(9,  2021, __file__)

#input = aoc.example
input = aoc.input
map = input.split()

# Part 1: check if basin, if so add to total risk
risk = 0
for i, l in enumerate(map):
    for j, e in enumerate(l):
        low = True
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if 0 <= i + di and i + di < len(map) and 0 <= j + dj and j + dj < len(map[0]) and (di != 0 or dj != 0) and (di == 0 or dj == 0):
                    if map[i + di][j + dj] <= e:
                        low = False

        if low:
            risk += (1 + int(e))

# Part 2
nb9 = sum([sum([1 if e == '9' else 0 for e in l])
          for l in map])  # nb of nine, will never get visited
seen = [[False for _ in range(len(map[0]))] for _ in range(
    len(map))]  # keep track of visited cells
nbseen = 0  # number of visited cells


def browse(i, j):
    global seen, nbseen

    # Mark cell visited
    seen[i][j] = True
    nbseen += 1

    c = 1  # Keep track of the number of cells added
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if 0 <= i + di and i + di < len(map) and 0 <= j + dj and j + dj < len(map[0]) and (di != 0 or dj != 0) and (di == 0 or dj == 0):
                if not seen[i + di][j + dj] and map[i + di][j + dj] != '9':
                    # Browse every non-9, non-visited neighbour
                    c += browse(i + di, j + dj)
    return c


# Browse the whole grid until full, put size of bassins in l
i, j = 0, 0
l = []
while nb9 + nbseen < len(map) * len(map[0]):
    if not seen[i][j] and map[i][j] != '9':
        l.append(browse(i, j))

    i += 1
    if i == len(map):
        i = 0
        j += 1

# Sort l. The three largest sizes are the three last elements
l.sort()
prod_bassins = l[-3] * l[-2] * l[-1]

print('Part 1:', risk)
#aoc.submit(1, risk)
print('Part 2:', prod_bassins)
#aoc.submit(2, prod_bassins)
