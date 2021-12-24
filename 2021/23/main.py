from aoc import AOC
from queue import PriorityQueue
from collections import defaultdict

aoc = AOC(23,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

amphipodToInt = lambda t: '.ABCD'.index(t)

def complete(grid):
    return all([all([el == i for el in grid[i]]) for i in range(1, len(grid))])

def hash(grid):
    return ''.join([''.join(map(str, grid[i])) for i in range(5)])

def copy(grid):
    return (grid[0][:], grid[1][:], grid[2][:], grid[3][:], grid[4][:])

def moves(grid):
    m = []
    
    # Try to put elements from the hallway in their rows
    for i in range(len(grid[0])):
        el = grid[0][i]
        if el != 0 and \
            all([grid[el][k] in [0, el] for k in range(len(grid[1]))]) and \
            all([grid[0][k] == 0 for k in range(min(i, 2 * el), max(i, 2 * el) + 1) if k != i]):
            try:
                future_pos = grid[el].index(el) - 1
            except:
                future_pos = len(grid[1]) - 1
            
            g = copy(grid)
            g[0][i] = 0
            g[el][future_pos] = el

            score = (abs(i - 2 * el) + future_pos + 1) * (10 ** (el - 1))

            m.append((score, g))
    
    # Try to put top elements from columns in the hallway
    for column in range(1, 5):
        if any(grid[column][k] != column for k in range(len(grid[1]))):
            for depth in range(len(grid[1])):
                if grid[column][depth] != 0:
                    for final_pos in [0, 1, 3, 5, 7, 9, 10]:
                        if all([grid[0][k] == 0 for k in range(min(final_pos, 2 * column), max(final_pos, 2 * column) + 1) if k != 2 * column]):
                            g = copy(grid)
                            g[0][final_pos] = grid[column][depth]
                            g[column][depth] = 0

                            score = (abs(final_pos - 2 * column) + depth + 1) * (10 ** (g[0][final_pos] - 1))

                            m.append((score, g))
                    break

    return m

def solve(grid):
    queue = PriorityQueue()
    queue.put((0, grid))
    seen = set()

    while not queue.empty():
        score, grid = queue.get()
        if complete(grid):
            return score
        if hash(grid) in seen:
            continue

        seen.add(hash(grid))

        for (new_score, new_grid) in moves(grid):
            queue.put((score + new_score, new_grid))

hallway = list(map(amphipodToInt, input[1][1:-1]))

c1 = list(map(amphipodToInt, [input[i][3] for i in range(2, len(input) - 1)]))
c2 = list(map(amphipodToInt, [input[i][5] for i in range(2, len(input) - 1)]))
c3 = list(map(amphipodToInt, [input[i][7] for i in range(2, len(input) - 1)]))
c4 = list(map(amphipodToInt, [input[i][9] for i in range(2, len(input) - 1)]))
grid = (hallway, c1, c2, c3, c4)
p1_sol = solve(grid)

c1 = c1[:1] + [4, 4] + c1[1:] # DD
c2 = c2[:1] + [3, 2] + c2[1:] # CB
c3 = c3[:1] + [2, 1] + c3[1:] # BA
c4 = c4[:1] + [1, 3] + c4[1:] # AC
grid = (hallway, c1, c2, c3, c4)
p2_sol = solve(grid)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
