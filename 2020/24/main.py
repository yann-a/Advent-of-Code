from aoc import AOC

aoc = AOC(24,  2020, __file__)

input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def neighbours(x, y):
    e = (x-1, y)
    w = (x+1, y)
    se = (x if y%2 == 0 else x+1, y-1)
    sw = (x-1 if y%2 == 0 else x, y-1)
    ne = (x if y%2 == 0 else x+1, y+1)
    nw = (x-1 if y%2 == 0 else x, y+1)

    return [e, w, se, sw, ne, nw]

def part1(instructions):
    flipped = {}
    for instruction in instructions:
        cursor = x = y = 0
        while cursor < len(instruction):
            if instruction[cursor] == 'e':
                x += 1
                cursor += 1
            elif instruction[cursor] == 'w':
                x -= 1
                cursor += 1
            elif instruction[cursor:cursor+2] == 'se':
                x += 0 if y%2 == 0 else 1
                y -= 1
                cursor += 2
            elif instruction[cursor:cursor+2] == 'sw':
                x -= 1 if y%2 == 0 else 0
                y -= 1
                cursor += 2
            elif instruction[cursor:cursor+2] == 'ne':
                x += 0 if y%2 == 0 else 1
                y += 1
                cursor += 2
            elif instruction[cursor:cursor+2] == 'nw':
                x -= 1 if y%2 == 0 else 0
                y += 1
                cursor += 2

        flipped[(x, y)] = flipped.get((x, y), 0) + 1

    nb_black = 0
    for (x, y) in flipped:
        if flipped[(x, y)] % 2 == 1:
            nb_black += 1

    return nb_black, flipped

def part2(flipped):
    miny, maxy = min([y for (_, y) in flipped]), max([y for (_, y) in flipped])
    minx, maxx = min([x for (x, _) in flipped]), max([x for (x, _) in flipped])

    for _ in range(100):
        miny, maxy, minx, maxx = miny-1, maxy+1, minx-1, maxx+1
        new_flip = {}

        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                flipped_neighbours = sum([1 if flipped.get(n, 0) % 2 == 1 else 0 for n in neighbours(x, y)])

                if (x, y) in flipped and flipped[(x, y)] % 2 == 1:
                    if flipped_neighbours in [1, 2]:
                        new_flip[(x, y)] = 1
                else:
                    if flipped_neighbours == 2:
                        new_flip[(x, y)] = 1

        flipped = new_flip

    return len(flipped)

p1_sol, flipped = part1(input)
p2_sol = part2(flipped)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
