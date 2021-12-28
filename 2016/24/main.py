from aoc import AOC
from queue import PriorityQueue

aoc = AOC(24,  2016, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def neighbours(x, y):
    neighs = []
    for d in [-1, 1]:
        if 0 <= x + d < len(input[0]) and input[y][x + d] != '#':
            neighs.append((x + d, y))
        if 0 <= y + d < len(input) and input[y + d][x] != '#':
            neighs.append((x, y + d))

    return neighs

x0 = y0 = None
max_poi = 0
for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] == '0':
            x0, y0 = x, y
        if input[y][x] not in ['.', '#']:
            max_poi = max(max_poi, int(max(input[y][x])))

queue = PriorityQueue()
queue.put((0, '0', x0, y0))
seen = set()
first_visit_len = return_len = None
while not queue.empty():
    (length, visited, x, y) = queue.get()
    
    if (visited, x, y) in seen:
        continue
    seen.add((visited, x, y))

    if input[y][x] not in ['.', '#']:
        if len(visited) == max_poi + 1 and input[y][x] == '0':
            return_len = length
            break

        if input[y][x] not in visited:
            visited += input[y][x]

        if len(visited) == max_poi + 1 and first_visit_len is None:
            first_visit_len = length

    for (nx, ny) in neighbours(x, y):
        queue.put((length + 1, visited, nx, ny))

p1_sol = first_visit_len
p2_sol = return_len

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
