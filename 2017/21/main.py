from aoc import AOC

aoc = AOC(21,  2017, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(3).strip().split('\n')

def flip(s):
    return '/'.join(ss[::-1] for ss in s.split('/'))

def rotate(s, n):
    p = [list(ss) for ss in s.split('/')]
    for _ in range(n):
        np = [l[::] for l in p]

        for i in range(len(np)):
            for j in range(len(np)):
                np[i][j] = p[len(np)-j-1][i]
        p = [ss[::] for ss in np]

    return '/'.join(''.join(ss) for ss in p)

def solve_n_iter(n):
    rules_2, rules_3 = [], []
    for line in input:
        sp = line.split(' => ')

        if len(sp[0].split('/')) == 2:
            rules_2.append((sp[0], sp[1].split('/')))
        else: # len(sp[0].split('/)) == 3:
            rules_3.append((sp[0], sp[1].split('/')))
    
    grid = [list('.#.'), list('..#'), list('###')]
    for i in range(n):
        print(f'{i}th iteration')
        l = len(grid)
        if l % 2 == 0:
            new_grid = [['.' for _ in range(l//2*3)] for _ in range(l//2*3)]

            for j in range(l // 2):
                for k in range(l // 2):
                    v = '/'.join(''.join(grid[j * 2 + dj][k * 2 + dk] for dk in range(2)) for dj in range(2))
                    for r in range(4):
                        p = rotate(v, r)
                        pf = rotate(flip(v), r)
                        for rule in rules_2:
                            if rule[0] == p or rule[0] == pf:
                                for dj in range(3):
                                    for dk in range(3):
                                        new_grid[j * 3 + dj][k * 3 + dk] = rule[1][dj][dk]
                            else:
                                p, pf

        else: # l % 3 == 0
            new_grid = [['.' for _ in range(l//3*4)] for _ in range(l//3*4)]

            for j in range(l // 3):
                for k in range(l // 3):
                    v = '/'.join(''.join(grid[j * 3 + dj][k * 3 + dk] for dk in range(3)) for dj in range(3))
                    for r in range(4):
                        p = rotate(v, r)
                        pf = rotate(flip(v), r)
                        for rule in rules_3:
                            if rule[0] == p or rule[0] == pf:
                                for dj in range(4):
                                    for dk in range(4):
                                        new_grid[j * 4 + dj][k * 4 + dk] = rule[1][dj][dk]

        grid = [ss[::] for ss in new_grid]

    return sum(l.count('#') for l in grid)

def part1():
    return solve_n_iter(5)

def part2():
    return solve_n_iter(18)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
