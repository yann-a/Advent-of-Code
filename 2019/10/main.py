from aoc import AOC
from collections import defaultdict
import math

aoc = AOC(10,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example().strip().split('\n')

def angle(center_x, center_y, touch_x, touch_y):
    if center_y == touch_y and touch_x < center_x: return 0

    delta_x = touch_x - center_x
    delta_y = center_y - touch_y
    theta_radians = math.atan2(delta_y, delta_x)
    return theta_radians + math.pi

def can_see(line, col, new_line, new_col):
    if input[line][col] == '.': return False
    if input[new_line][new_col] == '.': return False

    dline = abs(new_line - line)
    dcol = abs(new_col - col)

    if min(dline, dcol) > 0:
        dl = dline // math.gcd(dline, dcol)
        dc = dcol // math.gcd(dline, dcol)

        if line < new_line: lines = list(range(line, new_line + 1, dl))
        else: lines = list(range(line, new_line - 1, -dl))

        if col < new_col: cols = list(range(col, new_col + 1, dc))
        else: cols = list(range(col, new_col - 1, -dc))
    else:
        if dline == 0:
            if col < new_col: cols = list(range(col, new_col + 1))
            else: cols = list(range(col, new_col - 1, -1))
            lines = [line for _ in cols]
        else:
            if line < new_line: lines = list(range(line, new_line + 1))
            else: lines = list(range(line, new_line - 1, -1))
            cols = [col for _ in lines]

    if any(input[l][c] == '#' for (l, c) in list(zip(lines, cols))[1:-1]):
        return False

    return True

def part1():
    max_seen, best_location = 0, None
    for line in range(len(input)):
        for col in range(len(input[line])):
            seen = -1
            for new_line in range(len(input)):
                for new_col in range(len(input[new_line])):
                    seen += can_see(line, col, new_line, new_col)
            if seen > max_seen:
                max_seen = seen
                best_location = (line, col)

    return max_seen, best_location

def part2(best_location):
    line, col = best_location

    angles = defaultdict(list)
    for new_line in range(len(input)):
        for new_col in range(len(input[new_line])):
            if new_line == line and new_col == col: continue
            if input[new_line][new_col] == '.': continue
            
            angles[angle(line, col, new_line, new_col)].append((new_line, new_col))

    for a in angles:
        angles[a].sort(key=lambda p: (p[0] - line) ** 2 + (p[1] - col) ** 2)

    n = 0
    while True:
        for a in sorted(angles.keys()):
            if len(angles[a]) > 0:
                n += 1
                l, c = angles[a].pop(0)

                if n == 200:
                    return c * 100 + l

p1_sol, best_location = part1()
p2_sol = part2(best_location)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
