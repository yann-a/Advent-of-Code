from aoc import AOC
from collections import defaultdict

aoc = AOC(23,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

ORDER = [(-1, 1), (1, 1), (-1, 0), (1, 0)]

def draw_grid(elves):
    miny, maxy = min(y for y, x in elves), max(y for y, x in elves)
    minx, maxx = min(x for y, x in elves), max(x for y, x in elves)

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print('#' if (y, x) in elves else '.', end='')
        print()
    print()

def part1():
    elves = []
    for line in range(len(input)):
        for col in range(len(input[line])):
            if input[line][col] == '#':
                elves.append((line, col))

    draw_grid(elves)
    order_index = 0

    for _ in range(10):
        # Proposing phase
        proposed = defaultdict(list)
        proposes = {}
        for e in range(len(elves)):
            line, col = elves[e]

            if all((line+dline, col+dcol) not in elves for dline in range(-1, 2) for dcol in range(-1, 2) if dline != 0 or dcol != 0): continue
            for order in range(4):
                f, i = ORDER[(order_index + order) % 4]
                if all((line + (d if i == 0 else f), col + (d if i == 1 else f)) not in elves for d in range(-1, 2)):
                    proposed[(line + (0 if i == 0 else f), col + (0 if i == 1 else f))].append(e)
                    proposes[e] = (line + (0 if i == 0 else f), col + (0 if i == 1 else f))
                    break

        # Moving phase
        new_elves = []
        for e in range(len(elves)):
            if e in proposes and len(proposed[proposes[e]]) == 1:
                new_elves.append(proposes[e])
            else:
                new_elves.append(elves[e])

        elves = new_elves
        order_index += 1
        draw_grid(elves)

    miny, maxy = min(y for y, x in elves), max(y for y, x in elves)
    minx, maxx = min(x for y, x in elves), max(x for y, x in elves)

    s = 0
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (y, x) not in elves:
                s += 1

    return s

def part2():
    elves = []
    for line in range(len(input)):
        for col in range(len(input[line])):
            if input[line][col] == '#':
                elves.append((line, col))

    order_index = 0
    did_move = True

    while did_move:
        did_move = False
        # Proposing phase
        proposed = defaultdict(list)
        proposes = {}
        for e in range(len(elves)):
            line, col = elves[e]

            if all((line+dline, col+dcol) not in elves for dline in range(-1, 2) for dcol in range(-1, 2) if dline != 0 or dcol != 0): continue
            for order in range(4):
                f, i = ORDER[(order_index + order) % 4]
                if all((line + (d if i == 0 else f), col + (d if i == 1 else f)) not in elves for d in range(-1, 2)):
                    proposed[(line + (0 if i == 0 else f), col + (0 if i == 1 else f))].append(e)
                    proposes[e] = (line + (0 if i == 0 else f), col + (0 if i == 1 else f))
                    break

        # Moving phase
        new_elves = []
        for e in range(len(elves)):
            if e in proposes and len(proposed[proposes[e]]) == 1:
                new_elves.append(proposes[e])
                did_move = True
            else:
                new_elves.append(elves[e])

        elves = new_elves
        order_index += 1

    return order_index

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
