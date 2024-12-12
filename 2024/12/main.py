from aoc import AOC

aoc = AOC(12,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(3).strip().split('\n')

DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

h = len(input)
w = len(input[0])

def area(y, x, seen):
    area_cells = set()

    def dfs(y, x):
        area_cells.add((y, x))
        seen[y][x] = True

        for dy, dx in DIR4:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                if not seen[y + dy][x + dx] and input[y + dy][x + dx] == input[y][x]:
                    dfs(y + dy, x + dx)

    dfs(y, x)

    perimeter = 0
    for ny, nx in area_cells:
        nb = 0
        for dy, dx in DIR4:
            if (ny + dy, nx + dx) in area_cells:
                nb += 1
        perimeter += 4 - nb

    return len(area_cells) * perimeter

def part1():
    s = 0
    seen = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if not seen[y][x]:
                s += area(y, x, seen)

    return s

def area2(y, x, seen):
    area_cells = set()

    def dfs(y, x):
        area_cells.add((y, x))
        seen[y][x] = True

        for dy, dx in DIR4:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                if not seen[y + dy][x + dx] and input[y + dy][x + dx] == input[y][x]:
                    dfs(y + dy, x + dx)

    dfs(y, x)

    # Compite border cells inside shape with direction
    border = set()
    for cy, cx in area_cells:
        for dy, dx in DIR4:
            if (cy + dy, cx + dx) not in area_cells:
                border.add((cy, cx, dy, dx))

    # Horizontal or vertical dfs  on each side
    seen_border = set()
    def explore(by, bx, dy, dx):
        seen_border.add((by, bx, dy, dx))
        if dy == 0:
            for ddy in [-1, 1]:
                if (by + ddy, bx, dy, dx) in border and (by + ddy, bx, dy, dx) not in seen_border:
                    explore(by + ddy, bx, dy, dx)
        else:
            for ddx in [-1, 1]:
                if (by, bx + ddx, dy, dx) in border and (by, bx + ddx, dy, dx) not in seen_border:
                    explore(by, bx + ddx, dy, dx)

    sides = 0
    for (by, bx, dy, dx) in border:
        if (by, bx, dy, dx) not in seen_border:
            sides += 1
            explore(by, bx, dy, dx)

    return len(area_cells) * sides


def part2(): 
    s = 0
    seen = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if not seen[y][x]:
                s += area2(y, x, seen)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
