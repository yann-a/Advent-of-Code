from aoc import AOC
from collections import defaultdict
from functools import cache

aoc = AOC(16,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    flow_rates = {}
    graph = {}
    for line in input:
        line = line.split()

        valve = line[1]
        flow = int(line[4][5:-1])
        linked_to = ''.join(line[9:]).split(',')

        flow_rates[valve] = flow
        graph[valve] = linked_to

    TOTAL_TIME = 30

    states = [('AA', tuple(), 0)]
    best_flow = {}
    for minute in range(1, TOTAL_TIME + 1):
        new_states = []
        for valve, opened, pressure in states:
            if (valve, opened) in best_flow and pressure <= best_flow[(valve, opened)]: continue
            best_flow[(valve, opened)] = pressure

            flow_rate = flow_rates[valve]
            if valve not in opened and flow_rate > 0:
                new_opened = tuple(list(opened) + [valve])
                new_states.append((valve, new_opened, pressure + flow_rate * (TOTAL_TIME - minute)))
            for other_valve in graph[valve]:
                new_states.append((other_valve, opened, pressure))

        states = new_states

    return max(pressure for _, _, pressure in states)

def dfs(valve, remaining_time, opened_valves, pressure, elephant, flow_rates, distance):
    max_pressure = pressure
    for other_valve in distance[valve]:
        d = distance[valve][other_valve]
        if other_valve not in opened_valves and remaining_time > (d + 1):
            p = dfs(other_valve, remaining_time - (d + 1), opened_valves | set([other_valve]), pressure + (remaining_time - (d + 1)) * flow_rates[other_valve], elephant, flow_rates, distance)
            max_pressure = max(max_pressure, p)

    if elephant:
        p = dfs('AA', 26, opened_valves, pressure, False, flow_rates, distance)
        max_pressure = max(max_pressure, p)

    return max_pressure

def part2():
    # Parse input
    flow_rates = {}
    graph = {}
    for line in input:
        line = line.split()

        valve = line[1]
        flow = int(line[4][5:-1])
        linked_to = ''.join(line[9:]).split(',')

        flow_rates[valve] = flow
        graph[valve] = linked_to

    # Floyd-Warshall
    distance = {valve1: {valve2: 1_000_000 for valve2 in flow_rates} for valve1 in flow_rates}
    for valve1 in graph:
        for valve2 in graph[valve1]:
            distance[valve1][valve2] = 1
    for valve in flow_rates:
        distance[valve][valve] = 0
    for valve1 in flow_rates:
        for valve2 in flow_rates:
            for valve3 in flow_rates:
                if distance[valve2][valve3] > distance[valve2][valve1] + distance[valve1][valve3]:
                    distance[valve2][valve3] = distance[valve2][valve1] + distance[valve1][valve3]

    # Clean Floyd-Warshall graph
    distance = {valve1: {valve2: distance[valve1][valve2] for valve2 in distance[valve1] if flow_rates[valve2] and valve2 != valve1} for valve1 in distance if flow_rates[valve1] or valve1 == 'AA'}

    return dfs('AA', 26, set(), 0, True, flow_rates, distance)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
