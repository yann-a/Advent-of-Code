from aoc import AOC

aoc = AOC(25,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def move(grid, dir='>'):
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '>' and dir == '>':
                if grid[i][(j + 1) % len(grid[0])] == '.':
                    new_grid[i][(j + 1) % len(grid[0])] = '>'
                else:
                    new_grid[i][j] = '>'
            elif grid[i][j] == 'v' and dir == 'v':
                if grid[(i + 1) % len(grid)][j] == '.':
                    new_grid[(i + 1) % len(grid)][j] = 'v'
                else:
                    new_grid[i][j] = 'v'
            elif grid[i][j] != '.':
                new_grid[i][j] = grid[i][j]

    return new_grid

def solve():
    i = 0
    grid = list(map(list, input))
    while True:
        i += 1
        new_grid = move(grid, '>')
        new_grid = move(new_grid, 'v')

        if grid == new_grid:
            return i

        grid = new_grid

p1_sol = solve()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
