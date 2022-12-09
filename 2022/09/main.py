from aoc import AOC

aoc = AOC(9,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(3).strip().split('\n')
#input = aoc.get_example(7).strip().split('\n')

def part1():
    head = tail = (0, 0)
    tailpos = set([(0, 0)])

    for line in input:
        d, l = line.split()
        l = int(l)

        for _ in range(l):
            head = (head[0] + (d  == 'U') - (d == 'D'), head[1] + (d == 'R') - (d == 'L'))

            if head[0] == 2 + tail[0]:
                tail = (tail[0] + 1, head[1])
            elif head[0] == tail[0] - 2:
                tail = (tail[0] - 1, head[1])
            elif head[1] == 2 + tail[1]:
                tail = (head[0], tail[1] + 1)
            elif head[1] == tail[1] - 2:
                tail = (head[0], tail[1] - 1)
            tailpos.add(tail)

    return len(tailpos)

def cmp(a, b):
    if a > b: return 1
    elif a < b: return -1
    else: return 0

def part2():
    pos = [(0, 0) for _ in range(10)]
    tailpos = set([(0, 0)])

    for line in input:
        d, l = line.split()
        l = int(l)

        for _ in range(l):
            pos[-1] = (pos[-1][0] + (d  == 'U') - (d == 'D'), pos[-1][1] + (d == 'R') - (d == 'L'))

            for i in range(8, -1, -1):
                if pos[i+1][0] == 2 + pos[i][0]:
                    pos[i] = (pos[i][0] + 1, pos[i][1] + cmp(pos[i+1][1], pos[i][1]))
                elif pos[i+1][0] == pos[i][0] - 2:
                    pos[i] = (pos[i][0] - 1, pos[i][1] + cmp(pos[i+1][1], pos[i][1]))
                elif pos[i+1][1] == 2 + pos[i][1]:
                    pos[i] = (pos[i][0] + cmp(pos[i+1][0], pos[i][0]), pos[i][1] + 1)
                elif pos[i+1][1] == pos[i][1] - 2:
                    pos[i] = (pos[i][0] + cmp(pos[i+1][0], pos[i][0]), pos[i][1] - 1)
            tailpos.add(pos[0])

    return len(tailpos)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
