from aoc import AOC
from collections import defaultdict
from math import lcm

aoc = AOC(20,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

HIGH, LOW = True, False

def part1():
    graph = defaultdict(list)
    graph_p = defaultdict(list)
    for line in input:
        module, destinations = line.split(' -> ')
        destinations = destinations.split(', ')

        if module[0] in '&%':
            type = module[0]
            module = module[1:]
        else:
            type = 'b'

        graph[module] = (type, destinations)
        for destination in destinations:
            graph_p[destination].append(module)

    state = {}
    memory = {}
    for module in graph:
        if graph[module][0] == '%':
            state[module] = False
        elif graph[module][0] == '&':
            memory[module] = {m: LOW for m in graph_p[module]}

    c = [0, 0]
    for _ in range(1000):
        signals = [('button', 'broadcaster', LOW)]
        while len(signals) > 0:
            source, target, signal = signals.pop(0)
            c[signal] += 1

            #print(source, f'-{"high"if signal else"low"}->', target)

            if target not in graph:
                continue

            type, destinations = graph[target]

            if type == 'b':
                for destination in destinations:
                    signals.append((target, destination, signal))
            elif type == '%':
                if signal == LOW:
                    state[target] = not state[target]
                    for destination in destinations:
                        signals.append((target, destination, HIGH if state[target] else LOW))
            elif type == '&':
                memory[target][source] = signal
                new_signal = LOW if all(memory[target].values()) else HIGH
                for destination in destinations:
                    signals.append((target, destination, new_signal))

    return c[0] * c[1]       

def part2():
    graph = defaultdict(list)
    graph_p = defaultdict(list)
    for line in input:
        module, destinations = line.split(' -> ')
        destinations = destinations.split(', ')

        if module[0] in '&%':
            type = module[0]
            module = module[1:]
        else:
            type = 'b'

        graph[module] = (type, destinations)
        for destination in destinations:
            graph_p[destination].append(module)

    state = {}
    memory = {}
    for module in graph:
        if graph[module][0] == '%':
            state[module] = False
        elif graph[module][0] == '&':
            memory[module] = {m: LOW for m in graph_p[module]}

    assert(len(graph_p['rx']) == 1)
    rx_prev = graph_p['rx'][0]
    assert(graph[rx_prev][0] == '&')
    rx_prev_prev = graph_p[rx_prev]

    rx_prev_prev_nb_press = {}

    i = 0
    while len(rx_prev_prev_nb_press) < len(rx_prev_prev):
        i += 1
        signals = [('button', 'broadcaster', LOW)]
        while len(signals) > 0:
            source, target, signal = signals.pop(0)

            #print(source, f'-{"high"if signal else"low"}->', target)

            if target in rx_prev_prev and target not in rx_prev_prev_nb_press and signal == LOW:
                rx_prev_prev_nb_press[target] = i
            if target not in graph:
                continue

            type, destinations = graph[target]

            if type == 'b':
                for destination in destinations:
                    signals.append((target, destination, signal))
            elif type == '%':
                if signal == LOW:
                    state[target] = not state[target]
                    for destination in destinations:
                        signals.append((target, destination, HIGH if state[target] else LOW))
            elif type == '&':
                memory[target][source] = signal
                new_signal = LOW if all(memory[target].values()) else HIGH
                for destination in destinations:
                    signals.append((target, destination, new_signal))

    return lcm(*rx_prev_prev_nb_press.values())

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
