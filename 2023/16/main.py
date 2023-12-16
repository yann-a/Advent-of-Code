from aoc import AOC

aoc = AOC(16,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def countenergized(sy, sx, sd):
    H, W = len(input), len(input[0])

    beams = [(sy, sx, sd)]
    energized = [[False for _ in range(W)] for _ in range(H)]
    seen = set()

    while len(beams) > 0:
        y, x, d = beams.pop(0)

        if not (0 <= y < H and 0 <= x < W):
            continue

        if (y, x, d) in seen:
            continue

        energized[y][x] = True
        seen.add((y, x, d))

        tile = input[y][x]

        if tile == '.' or (tile == '|' and d in 'du') or (tile == '-' and d in 'lr'):
            nx = x + (d == 'r') - (d == 'l')
            ny = y + (d == 'd') - (d == 'u')
            beams.append((ny, nx, d))
        elif tile == '|':
            beams.append((y - 1, x, 'u'))
            beams.append((y + 1, x, 'd'))
        elif tile == '-':
            beams.append((y, x - 1, 'l'))
            beams.append((y, x + 1, 'r'))
        elif tile == '\\':
            if d == 'r': beams.append((y + 1, x, 'd'))
            if d == 'u': beams.append((y, x - 1, 'l'))
            if d == 'l': beams.append((y - 1, x, 'u'))
            if d == 'd': beams.append((y, x + 1, 'r'))
        elif tile == '/':
            if d == 'r': beams.append((y - 1, x, 'u'))
            if d == 'u': beams.append((y, x + 1, 'r'))
            if d == 'l': beams.append((y + 1, x, 'd'))
            if d == 'd': beams.append((y, x - 1, 'l'))

    return sum(sum(line) for line in energized)

def part1():
    return countenergized(0, 0, 'r')

def part2():
    m = 0

    for y in range(len(input)):
        m = max(m, countenergized(y, 0, 'r'))
        m = max(m, countenergized(y, len(input[0]) - 1, 'l'))
    for x in range(len(input[0])):
        m = max(m, countenergized(0, x, 'd'))
        m = max(m, countenergized(len(input) - 1, x, 'u'))

    return m

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
