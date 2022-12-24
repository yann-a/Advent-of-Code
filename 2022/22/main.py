from aoc import AOC

aoc = AOC(22,  2022, __file__)

input = aoc.input.rstrip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    map, instructions = input
    map = map.split('\n')

    max_len = max(len(line) for line in map)
    map = [line + ' ' * (max_len - len(line)) for line in map]

    y = 0
    x = min(map[0].index('.'), map[0].index('#'))
    d = 1

    ins_pos = 0

    while ins_pos < len(instructions):
        if instructions[ins_pos] in 'LR':
            d = (d + (instructions[ins_pos] == 'R') - (instructions[ins_pos] == 'L')) % 4
            ins_pos += 1
        else:
            il = instructions.index('L', ins_pos) if 'L' in instructions[ins_pos:] else -1
            ir = instructions.index('R', ins_pos) if 'R' in instructions[ins_pos:] else -1
            until = len(instructions)
            if il > 0: until = min(until, il)
            if ir > 0: until = min(until, ir)

            n = int(instructions[ins_pos:until])
            ins_pos = until

            nx, ny = x, y
            tx = (nx + (d == 1) - (d == 3)) % len(map[0])
            ty = (ny + (d == 2) - (d == 0)) % len(map)

            for _ in range(n):
                if map[ty][tx] == '.':
                    nx, ny = tx, ty
                    tx = (nx + (d == 1) - (d == 3)) % len(map[0])
                    ty = (ny + (d == 2) - (d == 0)) % len(map)
                elif map[ty][tx] == '#':
                    break
                else:
                    while map[ty][tx] == ' ':
                        tx = (tx + (d == 1) - (d == 3)) % len(map[0])
                        ty = (ty + (d == 2) - (d == 0)) % len(map)

                    if map[ty][tx] == '.':
                        nx, ny = tx, ty
                        tx = (nx + (d == 1) - (d == 3)) % len(map[0])
                        ty = (ny + (d == 2) - (d == 0)) % len(map)
                    else:
                        break

            x, y = nx, ny

    return 1000 * (y + 1) + 4 * (x + 1) + ((d + 3) % 4)

FACES = {'up': (100, 0), 'front': (150, 0), 'right': (100, 50), 'back': (50, 50), 'left': (0, 50), 'down': (0, 100)}
def overflow(x, y, d):
    face = [face for face in FACES if FACES[face][0] <= y < FACES[face][0] + 50 and FACES[face][1] <= x < FACES[face][1] + 50][0]
    nx = x + (d == 1) - (d == 3)
    ny = y + (d == 2) - (d == 0)
    nfaces = [face for face in FACES if FACES[face][0] <= ny < FACES[face][0] + 50 and FACES[face][1] <= nx < FACES[face][1] + 50]
    nface = None if len(nfaces) == 0 else nfaces[0]

    if face == nface: return nx, ny, d

    # Hardcoded using a paper reproduction of the cube from my input
    if face == 'up' and d == 0: nx, ny, d = 50, 50 + nx, 1
    elif face == 'up' and d == 1: pass
    elif face == 'up' and d == 2: pass
    elif face == 'up' and d == 3: nx, ny, d = 50, 149 - ny, 1
    elif face == 'front' and d == 0: pass
    elif face == 'front' and d == 1: nx, ny, d = y - 100, 149, 0
    elif face == 'front' and d == 2: nx, ny, d = nx + 100, 0, 2
    elif face == 'front' and d == 3: nx, ny, d = ny - 100, 0, 2
    elif face == 'right' and d == 0: pass
    elif face == 'right' and d == 1: nx, ny, d = 149, 149 - ny, 3
    elif face == 'right' and d == 2: nx, ny, d = 49, nx + 100, 3
    elif face == 'right' and d == 3: pass
    elif face == 'left' and d == 0: nx, ny, d = 0, nx + 100, 1
    elif face == 'left' and d == 1: pass
    elif face == 'left' and d == 2: pass
    elif face == 'left' and d == 3: nx, ny, d = 0, 149 - ny, 1
    elif face == 'back' and d == 0: pass
    elif face == 'back' and d == 1: nx, ny, d = ny + 50, 49, 0
    elif face == 'back' and d == 2: pass
    elif face == 'back' and d == 3: nx, ny, d = ny - 50, 100, 2
    elif face == 'down' and d == 0: nx, ny, d = nx - 100, 199, 0
    elif face == 'down' and d == 1: nx, ny, d = 99, 149 - ny, 3
    elif face == 'down' and d == 2: nx, ny, d = 99, nx - 50, 3
    elif face == 'down' and d == 3: pass

    return nx, ny, d

def part2():
    map, instructions = input
    map = map.split('\n')

    max_len = max(len(line) for line in map)
    map = [line + ' ' * (max_len - len(line)) for line in map]

    y = 0
    x = min(map[0].index('.'), map[0].index('#'))
    d = 1

    ins_pos = 0

    while ins_pos < len(instructions):
        if instructions[ins_pos] in 'LR':
            d = (d + (instructions[ins_pos] == 'R') - (instructions[ins_pos] == 'L')) % 4
            ins_pos += 1
        else:
            il = instructions.index('L', ins_pos) if 'L' in instructions[ins_pos:] else -1
            ir = instructions.index('R', ins_pos) if 'R' in instructions[ins_pos:] else -1
            until = len(instructions)
            if il > 0: until = min(until, il)
            if ir > 0: until = min(until, ir)

            n = int(instructions[ins_pos:until])
            ins_pos = until

            nx, ny, nd = x, y, d
            tx, ty, td = overflow(x, y, d)

            for _ in range(n):
                if map[ty][tx] == '.':
                    nx, ny, nd = tx, ty, td
                    tx, ty, td = overflow(nx, ny, nd)
                elif map[ty][tx] == '#':
                    break

            x, y, d = nx, ny, nd

    return 1000 * (y + 1) + 4 * (x + 1) + ((d + 3) % 4)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
