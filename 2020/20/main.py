from aoc import AOC
from functools import reduce
import math

aoc = AOC(20,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

# Gather tiles and relations
tiles, edges, graph = {}, {}, {}
for tile in input:
    lines = tile.split('\n')
    id = int(lines[0][:-1].split()[1])

    tiles[id] = lines[1:]
    edges[id] = edges.get(id, []) + [lines[1], lines[-1], ''.join(lines[i][0] for i in range(1, len(lines))), ''.join(lines[i][-1] for i in range(1, len(lines)))]
    graph[id] = set()

    for other_tile in tiles:
        if other_tile != id:
            for i_id, edge in enumerate(edges[id]):
                for i_other, other_edge in enumerate(edges[other_tile]):
                    if edge == other_edge or edge == other_edge[::-1]:
                        graph[id].add((i_id, i_other, other_tile))
                        graph[other_tile].add((i_other, i_id, id))

# The corner pieces have only 2 neighbours
product = reduce(lambda x, y: x * y, [id for id in tiles if len(graph[id]) == 2])

# We place the pieces top left to bottom right
N = int(math.sqrt(len(tiles)))
grid = [[0 for _ in range(N)] for _ in range(N)]
grid_ids = [[0 for _ in range(N)] for _ in range(N)]
placed = {id: False for id in tiles}

line, col = 0, 0
while line < N:
    if line == 0 and col == 0:
        # First tile: we pick a corner, and rotate it so that the two faces that are shared are bottom and left ones
        for tile in tiles:
            if len(graph[tile]) == 2:
                common_edges = sorted([i_id for (i_id, _, _) in graph[tile]])
                if common_edges == [0, 2]:
                    grid[0][0] = [[tiles[tile][i][j] for j in range(len(tiles[tile][0]) - 1, -1, -1)] for i in range(len(tiles[tile]) - 1, -1, -1)]
                elif common_edges == [0, 3]:
                    grid[0][0] = [[tiles[tile][j][i] for j in range(len(tiles[tile]) - 1, -1, -1)] for i in range(len(tiles[tile][0]))]
                elif common_edges == [1, 2]:
                    grid[0][0] = [[tiles[tile][j][i] for j in range(len(tiles[tile]))] for i in range(len(tiles[tile][0]) - 1, -1, -1)]
                elif common_edges == [1, 3]:
                    grid[0][0] = tiles[tile]

                grid_ids[0][0] = tile
                placed[tile] = True
                break
    elif line == 0 and col > 0:
        # We have a tile to the left: we pick the correct one out of its neighbours, rotate it to have the correct face facing
        # left, and then finally we flip it upside down if needed
        left_col_prev = ''.join(grid[line][col - 1][i][-1] for i in range(len(grid[line][col - 1])))
        for (_, i_other, other_tile) in graph[grid_ids[line][col - 1]]:
            if not placed[other_tile]:
                if left_col_prev in edges[other_tile] or left_col_prev[::-1] in edges[other_tile]:
                    if i_other == 0:
                        grid[line][col] = [[tiles[other_tile][j][i] for j in range(len(tiles[other_tile]))] for i in range(len(tiles[other_tile][0]) - 1, -1, -1)]
                    elif i_other == 1:
                        grid[line][col] = [[tiles[other_tile][j][i] for j in range(len(tiles[other_tile]) - 1, -1, -1)] for i in range(len(tiles[other_tile][0]))]
                    elif i_other == 2:
                        grid[line][col] = tiles[other_tile]
                    elif i_other == 3:
                        grid[line][col] = [tiles[other_tile][i][::-1] for i in range(len(tiles[other_tile]))]

                    if left_col_prev != ''.join(grid[line][col][i][0] for i in range(len(grid[line][col]))):
                        grid[line][col] = grid[line][col][::-1]

                    grid_ids[line][col] = other_tile
                    placed[other_tile] = True
                    break
    else:
        # We don't have a tile to the left, but we have one above : almost the same thing
        bot_row_prev = ''.join(grid[line - 1][col][-1])
        for (_, i_other, other_tile) in graph[grid_ids[line - 1][col]]:
            if not placed[other_tile]:
                if bot_row_prev in edges[other_tile] or bot_row_prev[::-1] in edges[other_tile]:
                    if i_other == 0:
                        grid[line][col] = tiles[other_tile]
                    elif i_other == 1:
                        grid[line][col] = tiles[other_tile][::-1]
                    elif i_other == 2:
                        grid[line][col] = [[tiles[other_tile][j][i] for j in range(len(tiles[other_tile]) - 1, -1, -1)] for i in range(len(tiles[other_tile][0]))]
                    elif i_other == 3:
                        grid[line][col] = [[tiles[other_tile][j][i] for j in range(len(tiles[other_tile]))] for i in range(len(tiles[other_tile][0]) - 1, -1, -1)]

                    if bot_row_prev != ''.join(grid[line][col][0]):
                        grid[line][col] = [grid[line][col][i][::-1] for i in range(len(grid[line][col]))]

                    grid_ids[line][col] = other_tile
                    placed[other_tile] = True
                    break

    col += 1
    if col == N:
        line += 1
        col = 0

def printGrid(grid, N):
    for abs_line in range(N):
        for line in range(len(grid[0][0])):
            for abs_col in range(N):
                print(''.join(grid[abs_line][abs_col][line]) + ' ', end='')
            print()
        print()
#printGrid(grid, N)

# Recreate image without borders
image = []
for abs_line in range(N):
    for line in range(1, len(grid[0][0]) - 1):
        line_str = ''
        for abs_col in range(N):
            for col in range(1, len(grid[0][0][0]) - 1):
                line_str += grid[abs_line][abs_col][line][col]
        image.append(line_str)

# Search for monsters
monster = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
part_of_a_sea_monster = [[False for x in line] for line in image]

# Exhaustive search, for every flip and rotation of the board
for i in range(8):
    if i % 4 == 0:
        image = image[::-1]
        part_of_a_sea_monster = part_of_a_sea_monster[::-1]
    
    for y in range(len(image)):
        for x in range(len(image[0])):
            is_monster = True
            for (dx, dy) in monster:
                if not(0 <= y + dy < len(image) and 0 <= x + dx < len(image[0]) and image[y + dy][x + dx] == '#'):
                    is_monster = False
            if is_monster:
                for (dx, dy) in monster:
                    part_of_a_sea_monster[y + dy][x + dx] = True

    image = [[image[j][i] for j in range(len(image) - 1, -1, -1)] for i in range(len(image[0]))]
    part_of_a_sea_monster = [[part_of_a_sea_monster[j][i] for j in range(len(image) - 1, -1, -1)] for i in range(len(image[0]))]

roughness = sum([sum([1 if not part_of_a_sea_monster[y][x] and image[y][x] == '#' else 0 for x in range(len(image[0]))]) for y in range(len(image))])

p1_sol = product
p2_sol = roughness

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
