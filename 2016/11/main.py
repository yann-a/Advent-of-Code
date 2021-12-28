from aoc import AOC
from queue import PriorityQueue

aoc = AOC(11,  2016, __file__)

floors = [ # input
    set([('thulium', 'g'), ('thulium', 'm'), ('plutonium', 'g'), ('strontium', 'g')]),
    set([('plutonium', 'm'), ('strontium', 'm')]),
    set([('promethium', 'g'), ('promethium', 'm'), ('ruthenium', 'g'), ('ruthenium', 'm')]),
    set()
]

def serialize(floors):
    return '___'.join(['__'.join([a + '_' + b for (a, b) in sorted(floor)]) for floor in floors])

def deserialize(floors):
    floors = floors.split('___')
    floors = [floor.split('__') for floor in floors]
    floors = [set([tuple(element.split('_')) for element in floor if element != '']) for floor in floors]
    return floors

def isComplete(floors):
    return all([len(floor) == 0 for floor in floors[:-1]])

def isStable(floors):
    for floor in floors:
        for (element, type) in floor:
            if type == 'm' and any([t == 'g' for (e, t) in floor]) and (element, 'g') not in floor:
                return False
    return True

def nextConfigs(floors, elevator_pos):
    next_configs = []

    for element1 in floors[elevator_pos]:
        if elevator_pos > 0:
            f = [floor.copy() for floor in floors]
            f[elevator_pos - 1].add(element1)
            f[elevator_pos].remove(element1)

            if isStable(f):
                next_configs.append((elevator_pos - 1, f))
        if elevator_pos < 3:
            f = [floor.copy() for floor in floors]
            f[elevator_pos + 1].add(element1)
            f[elevator_pos].remove(element1)

            if isStable(f):
                next_configs.append((elevator_pos + 1, f))

    for element1 in floors[elevator_pos]:
        for element2 in floors[elevator_pos]:
            if element1 != element2:
                if elevator_pos > 0:
                    f = [floor.copy() for floor in floors]
                    f[elevator_pos - 1].add(element1)
                    f[elevator_pos - 1].add(element2)
                    f[elevator_pos].remove(element1)
                    f[elevator_pos].remove(element2)

                    if isStable(f):
                        next_configs.append((elevator_pos - 1, f))
                if elevator_pos < 3:
                    f = [floor.copy() for floor in floors]
                    f[elevator_pos + 1].add(element1)
                    f[elevator_pos + 1].add(element2)
                    f[elevator_pos].remove(element1)
                    f[elevator_pos].remove(element2)

                    if isStable(f):
                        next_configs.append((elevator_pos + 1, f))

    return next_configs

def solve(floors):
    queue = PriorityQueue()
    queue.put((0, 0, serialize(floors)))
    seen = set()

    while not queue.empty():
        (nb_steps, elevator_pos, floors) = queue.get()

        if (elevator_pos, floors) in seen:
            continue
        seen.add((elevator_pos, floors))

        floors = deserialize(floors)

        if isComplete(floors):
            return nb_steps

        for (next_elevator_pos, next_config) in nextConfigs(floors, elevator_pos):
            queue.put((nb_steps + 1, next_elevator_pos, serialize(next_config)))

p1_sol = solve(floors)
print(p1_sol)

floors[0] = floors[0].union(set([('elerium', 'g'), ('elerium', 'm'), ('dilithium', 'g'), ('dilithium', 'm')]))
p2_sol = solve(floors)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
