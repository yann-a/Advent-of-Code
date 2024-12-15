from aoc import AOC

aoc = AOC(15,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

M = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def part1():
    map = [list(line) for line in input[0].split('\n')]
    moves = ''.join(input[1].split('\n'))

    h, w = len(map), len(map[0])

    for y in range(h):
        for x in range(w):
            if map[y][x] == '@':
                map[y][x] = '.'
                by, bx = y, x

    for move in moves:
        dy, dx = M[move]

        desty, destx = by + dy, bx + dx
        crates_to_move = set()
        while map[desty][destx] != '.':
            if map[desty][destx] == '#':
                break
            crates_to_move.add((desty,destx))
            desty, destx = desty + dy, destx + dx
        else:
            by, bx = by + dy, bx + dx
            for cy, cx in crates_to_move:
                map[cy][cx] = '.'
            for cy, cx in crates_to_move:
                map[cy + dy][cx + dx]  = 'O'

    s = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == 'O':
                s += 100 * y + x

    return s

def print_grid(by, bx, map):
    for y in range(h):
        for x in range(w):
            if (y, x) == (by, bx): print('@', end='')
            else: print(map[y][x], end='')
        print()
    print()

def part2():
    map = [[e if e != 'O' else ['[', ']'][i] for e in line for i in range(2)] for line in input[0].split('\n')]
    moves = ''.join(input[1].split('\n'))

    h, w = len(map), len(map[0])

    by, bx = None, None
    for y in range(h):
        for x in range(w):
            if map[y][x] == '@':
                map[y][x] = '.'
                if by is None:
                    by, bx = y, x

    for move in moves:
        dy, dx = M[move]

        pos_to_check = set([(by + dy, bx + dx)])
        crates_to_move = set()
        while not all(map[py][px] == '.' for py, px in pos_to_check):
            if any(map[py][px] == '#' for py, px in pos_to_check):
                break

            new_pos_to_check = set()
            for py, px in pos_to_check:
                if map[py][px] == '[':
                    crates_to_move.add((py, px))
                    if move in '^v':
                        new_pos_to_check.add((py + dy, px + dx))
                        new_pos_to_check.add((py + dy, px + 1 + dx))
                    else:
                        new_pos_to_check.add((py + dy, px + 2*dx))
                elif map[py][px] == ']':
                    crates_to_move.add((py, px - 1))
                    if move in '^v':
                        new_pos_to_check.add((py + dy, px + dx))
                        new_pos_to_check.add((py + dy, px - 1 + dx))
                    else:
                        new_pos_to_check.add((py + dy, px + 2*dx))

            pos_to_check = new_pos_to_check
        else:
            by, bx = by + dy, bx + dx
            for cy, cx in crates_to_move:
                map[cy][cx] = '.'
                map[cy][cx + 1] = '.'
            for cy, cx in crates_to_move:
                map[cy + dy][cx + dx]  = '['
                map[cy + dy][cx + 1 + dx] = ']'

    s = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == '[':
                s += 100 * y + x

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
