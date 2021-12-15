from functools import reduce

lines = [((int(l[0]), int(l[1])), (int(l[3]), int(l[4]))) for line in open('input') if (l := line.replace(',', ' ').split())]

Mx = reduce(lambda mx, line: max(mx, line[0][0], line[1][0]), lines, 0)
My = reduce(lambda my, line: max(my, line[0][1], line[1][1]), lines, 0)

grid_1 = [[0 for _ in range(Mx + 1)] for _ in range(My + 1)]
grid_2 = [[0 for _ in range(Mx + 1)] for _ in range(My + 1)]

for line in lines:
    if line[0][0] == line[1][0]:
        sy, ey = (line[0][1], line[1][1]) if line[0][1] < line[1][1] else (line[1][1], line[0][1])
        for y in range(sy, ey + 1):
            grid_1[y][line[0][0]] += 1
            grid_2[y][line[0][0]] += 1
    elif line[0][1] == line[1][1]:
        sx, ex = (line[0][0], line[1][0]) if line[0][0] < line[1][0] else (line[1][0], line[0][0])
        for x in range(sx, ex + 1):
            grid_1[line[0][1]][x] += 1
            grid_2[line[0][1]][x] += 1
    else:
        # If line at pi/4 rad
        if line[0][0] + line[0][1] == line[1][0] + line[1][1]:
            sx, sy = line[0] if line[0][0] < line[1][0] else line[1]
            for i in range(max(abs(sx - line[0][0]), abs(sx - line[1][0])) + 1):
                grid_2[sy - i][sx + i] += 1
        # If line at -pi/4 rad
        else:
            sx, sy = line[0] if line[0][0] < line[1][0] else line[1]
            for i in range(max(abs(sx - line[0][0]), abs(sx - line[1][0])) + 1):
                grid_2[sy + i][sx + i] += 1

nb_sup2_1 = reduce(lambda n, row: n + reduce(lambda m, pos: m + 1 if pos >= 2 else m, row, 0), grid_1, 0)
nb_sup2_2 = reduce(lambda n, row: n + reduce(lambda m, pos: m + 1 if pos >= 2 else m, row, 0), grid_2, 0)
print('Part 1:', nb_sup2_1)
print('Part 2:', nb_sup2_2)
