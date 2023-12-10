from aoc import AOC

aoc = AOC(10,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

H, W = len(input), len(input[0])

def part1():
    for y in range(H):
        for x in range(W):
            if input[y][x] == 'S':
                ay, ax = y, x

    loop = [(ay, ax)]
    d = 'S' # found by hand in the input
    ny, nx = ay + 1, ax # same

    while (ny, nx) != loop[0]:
        loop.append((ny, nx))

        if input[ny][nx] == '|':
            ny = ny + (1 if d == 'S' else -1)
        elif input[ny][nx] == '-':
            nx = nx + (1 if d == 'E' else -1)
        elif input[ny][nx] == '7':
            if d == 'E':
                d = 'S'
                ny += 1
            else:
                d = 'W'
                nx -= 1
        elif input[ny][nx] == 'J':
            if d == 'E':
                d = 'N'
                ny -= 1
            else:
                d = 'W'
                nx -= 1
        elif input[ny][nx] == 'F':
            if d == 'N':
                d = 'E'
                nx += 1
            else:
                d = 'S'
                ny += 1
        elif input[ny][nx] == 'L':
            if d == 'S':
                d = 'E'
                nx += 1
            else:
                d = 'N'
                ny -= 1

    return len(loop) // 2

def part2():
    s = 0

    for y in range(H):
        status = 1
        for x in range(W):
            if input[y][x] == '.':
                s += status
            elif status == 1:
                status = 0
            elif input[y][x] in '|7J':
                status = 1

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)