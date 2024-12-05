from aoc import AOC
from collections import defaultdict

aoc = AOC(5,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    rules, updates = input
    
    graph = defaultdict(list)
    rules = rules.split('\n')
    for line in rules:
        a, b = map(int, line.split('|'))
        graph[b].append(a)

    updates = list(map(lambda line: list(map(int, line.split(','))), updates.split('\n')))

    def check_update(update):
        for i in range(len(update)):
            for previous in graph[update[i]]:
                if previous in update and not previous in update[:i]:
                    return False
        return True

    s = 0
    for update in updates:
        if check_update(update):
            s += update[len(update) // 2]

    return s

def part2():
    rules, updates = input
    
    graph = defaultdict(list)
    rules = rules.split('\n')
    for line in rules:
        a, b = map(int, line.split('|'))
        graph[b].append(a)

    updates = list(map(lambda line: list(map(int, line.split(','))), updates.split('\n')))

    def check_update(update):
        for i in range(len(update)):
            for previous in graph[update[i]]:
                if previous in update and not previous in update[:i]:
                    return False
        return True

    s = 0
    for update in updates:
        if check_update(update):
            continue

        # Topological sort
        new_order = []
        def push_node(node):
            for previous in graph[node]:
                if previous in update and previous not in new_order:
                    push_node(previous)
            if node not in new_order:
                new_order.append(node)

        for node in update:
            push_node(node)

        s += new_order[len(update) // 2]

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
