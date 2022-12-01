from aoc import AOC

aoc = AOC(7,  2017, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

graph = {}
for line in input:
    parts = line.split(' -> ')

    if len(parts) == 1:
        parts.append('')

    parts[0] = parts[0].split()
    parts[1] = parts[1].split(', ')

    graph[parts[0][0]] = (parts[1] if parts[1][0] != '' else [], int(parts[0][1][1:-1]))

root = None
for program in graph:
    if all([program not in graph[parent][0] for parent in graph]):
        root = program

def balance(root):
    child_balance = [balance(child) for child in graph[root][0]]

    for (b, v) in child_balance:
        if not b:
            return False, v
    
    if len(child_balance) > 2:
        for i, (b, v) in enumerate(child_balance):
            if i == 0:
                if child_balance[0][1] != child_balance[1][1] and child_balance[1][1] == child_balance[2][1]:
                    return False, child_balance[1][1] - child_balance[0][1] + graph[graph[root][0][0]][1]
            elif i == 1:
                if child_balance[0][1] != child_balance[1][1] and child_balance[0][1] == child_balance[2][1]:
                    return False, child_balance[0][1] - child_balance[1][1] + graph[graph[root][0][1]][1]
            else:
                if child_balance[0][1] != child_balance[i][1]:
                    return False, child_balance[0][1] - child_balance[i][1] + graph[graph[root][0][i]][1]

    if len(child_balance) == 0:
        return True, graph[root][1]

    return True, graph[root][1] + sum([cb[1] for cb in child_balance])

p1_sol = root
p2_sol = balance(root)[1]

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)