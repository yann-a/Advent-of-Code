from aoc import AOC

aoc = AOC(13,  2018, __file__)

input = aoc.input.split('\n')[:-1]
#input = open('example', 'r').read().split('\n')[:-1]

deflect = {
    '/': [1, 0, 3, 2],
    '\\': [3, 2, 1, 0]
}

def part1():
    map = input[:]

    carts = {}
    for i, line in enumerate(map):
        for j, col in enumerate(line):
            if col == '^':
                carts[(i, j)] = (0, 0)
                map[i] = map[i][:j] + '|' + map[i][j+1:]
            elif col == '>':
                carts[(i, j)] = (1, 0)
                map[i] = map[i][:j] + '-' + map[i][j+1:]
            elif col == 'v':
                carts[(i, j)] = (2, 0)
                map[i] = map[i][:j] + '|' + map[i][j+1:]
            elif col == '<':
                carts[(i, j)] = (3, 0)
                map[i] = map[i][:j] + '-' + map[i][j+1:]

    while True:
        carts_l = sorted(carts.keys())
        
        for (i, j) in carts_l:
            orientation, next_turn = carts[(i, j)]

            ni = i + (orientation == 2) - (orientation == 0)
            nj = j + (orientation == 1) - (orientation == 3)

            if (ni, nj) in carts:
                return f'{nj},{ni}'

            if map[ni][nj] in deflect:
                orientation = deflect[map[ni][nj]][orientation]
            elif map[ni][nj] == '+':
                if next_turn == 0:
                    orientation = (orientation - 1) % 4
                elif next_turn == 2:
                    orientation = (orientation + 1) % 4

                next_turn = (next_turn + 1) % 3

            del carts[(i, j)]
            carts[(ni, nj)] = (orientation, next_turn)

def part2():
    map = input[:]

    carts = {}
    for i, line in enumerate(map):
        for j, col in enumerate(line):
            if col == '^':
                carts[(i, j)] = (0, 0)
                map[i] = map[i][:j] + '|' + map[i][j+1:]
            elif col == '>':
                carts[(i, j)] = (1, 0)
                map[i] = map[i][:j] + '-' + map[i][j+1:]
            elif col == 'v':
                carts[(i, j)] = (2, 0)
                map[i] = map[i][:j] + '|' + map[i][j+1:]
            elif col == '<':
                carts[(i, j)] = (3, 0)
                map[i] = map[i][:j] + '-' + map[i][j+1:]

    print(carts)

    while True:
        carts_l = sorted(carts.keys())
        
        for (i, j) in carts_l:
            if (i, j) not in carts:
                continue

            orientation, next_turn = carts[(i, j)]

            ni = i + (orientation == 2) - (orientation == 0)
            nj = j + (orientation == 1) - (orientation == 3)

            if (ni, nj) in carts:
                del carts[(i, j)]
                del carts[(ni, nj)]
                continue

            if map[ni][nj] in deflect:
                orientation = deflect[map[ni][nj]][orientation]
            elif map[ni][nj] == '+':
                if next_turn == 0:
                    orientation = (orientation - 1) % 4
                elif next_turn == 2:
                    orientation = (orientation + 1) % 4

                next_turn = (next_turn + 1) % 3

            del carts[(i, j)]
            carts[(ni, nj)] = (orientation, next_turn)

        if len(carts) <= 1:
            break

    for (i, j) in carts:
        return f'{j},{i}'

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
