from aoc import AOC

aoc = AOC(14,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

H = 103
W = 101

def part1():
    robots = [[0] * W for _ in range(H)]

    for bot in input:
        p, v = bot.split()
        p = list(map(int, p[2:].split(',')))
        v = list(map(int, v[2:].split(',')))

        for _ in range(100):
            p[0] = (p[0] + v[0]) % W
            p[1] = (p[1] + v[1]) % H

        robots[p[1]][p[0]] += 1

    q1 = sum(robots[y][x] for y in range(H // 2) for x in range(W // 2))
    q2 = sum(robots[y][x] for y in range(H // 2) for x in range(W // 2 + 1, W))
    q3 = sum(robots[y][x] for y in range(H // 2 + 1, H) for x in range(W // 2))
    q4 = sum(robots[y][x] for y in range(H // 2 + 1, H) for x in range(W // 2 + 1, W))

    return q1 * q2 * q3 * q4

def pic_connected(robots, threshold):
    DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    isolated = 0
    for y in range(H):
        for x in range(W):
            if robots[y][x] > 0:
                if all(robots[(y + dy) % H][(x + dx) % W] == 0 for dy, dx in DIR8):
                    isolated += 1
    
    return isolated < threshold

def part2():
    robots = [[0] * W for _ in range(H)]
    bots = []

    # Obtained by manual adjustments
    threshold = 150

    for bot in input:
        p, v = bot.split()
        p = list(map(int, p[2:].split(',')))
        v = list(map(int, v[2:].split(',')))

        bots.append([p, v])
        robots[p[1]][p[0]] += 1

    it = 0
    while True:
        it += 1
        for p, v in bots:
            robots[p[1]][p[0]] -= 1

            p[0] = (p[0] + v[0]) % W
            p[1] = (p[1] + v[1]) % H

            robots[p[1]][p[0]] += 1

        if pic_connected(robots, threshold):
            print('Iterations: ', it)
            for y in range(H):
                for x in range(W):
                    print('*' if robots[y][x] > 0 else ' ', end='')
                print()   
            print() 
            
            return it

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
