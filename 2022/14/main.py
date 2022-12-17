from aoc import AOC

aoc = AOC(14,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def print_grid(walls, sand, maxy, minx, maxx, iswall = False, dx = None, dy = None):
    for y in range(0, maxy + (3 if iswall else 0)):
        for x in range(minx, maxx + 1):
            if (x, y) in walls or y == maxy + 2:
                print('#', end='')
            elif (x, y) in sand:
                print('o', end='')
            elif dx is not None and dy is not None and x == dx and y == dy:
                print('+', end='')
            else:
                print('.', end='')
        print()
    print()

def part1():
    walls = set()
    maxy = 0
    minx, maxx = 1_000_000, -1_000_000
    for line in input:
        path_elements = line.split(' -> ')
        for i in range(len(path_elements) - 1):
            el1x, el2y = map(int, path_elements[i].split(','))
            el2x, el1y = map(int, path_elements[i+1].split(','))

            if el1x == el2x:
                for y in range(min(el1y, el2y), max(el1y, el2y) + 1):
                    walls.add((el1x, y))
                maxy = max(maxy, max(el1y, el2y))
                minx = min(minx, el1x)
                maxx = max(maxx, el1x)
            else:
                for x in range(min(el1x, el2x), max(el1x, el2x) + 1):
                    walls.add((x, el1y))
                maxy = max(maxy, el1y)
                minx = min(minx, min(el1x, el2x))
                maxx = max(maxx, max(el1x, el2x))

    sand = set()
    while True:
        x, y = 500, 0
        l_sand = len(sand)
        while y <= maxy:
            if (x, y + 1) not in walls and (x, y + 1) not in sand:
                y += 1
            elif (x - 1, y +1) not in walls and (x - 1, y + 1) not in sand:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in walls and (x + 1, y + 1) not in sand:
                x += 1
                y += 1
            else:
                sand.add((x, y))
                break

        if len(sand) == l_sand:
            break

    #print_grid(walls, sand, maxy, minx-45, maxx+45)

    return len(sand)

def part2():
    walls = set()
    maxy = 0
    minx, maxx = 1_000_000, -1_000_000
    for line in input:
        path_elements = line.split(' -> ')
        for i in range(len(path_elements) - 1):
            el1x, el2y = map(int, path_elements[i].split(','))
            el2x, el1y = map(int, path_elements[i+1].split(','))

            if el1x == el2x:
                for y in range(min(el1y, el2y), max(el1y, el2y) + 1):
                    walls.add((el1x, y))
                maxy = max(maxy, max(el1y, el2y))
                minx = min(minx, el1x)
                maxx = max(maxx, el1x)
            else:
                for x in range(min(el1x, el2x), max(el1x, el2x) + 1):
                    walls.add((x, el1y))
                maxy = max(maxy, el1y)
                minx = min(minx, min(el1x, el2x))
                maxx = max(maxx, max(el1x, el2x))

    sand = set()
    while True:
        x, y = 500, 0
        l_sand = len(sand)
        while True:
            if (x, y + 1) not in walls and (x, y + 1) not in sand and y + 1 != maxy + 2:
                y += 1
            elif (x - 1, y +1) not in walls and (x - 1, y + 1) not in sand and y + 1 != maxy + 2:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in walls and (x + 1, y + 1) not in sand and y + 1 != maxy + 2:
                x += 1
                y += 1
            else:
                sand.add((x, y))
                break

        if y == 0:
            break

    #print_grid(walls, sand, maxy, minx-45, maxx+45, True)

    return len(sand)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
