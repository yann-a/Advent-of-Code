from aoc import AOC
from functools import cache

aoc = AOC(19,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

blueprints = []
for blueprint in input:
    blueprint_id = int(blueprint[blueprint.index(' ')+1:blueprint.index(':')])
    blueprint = blueprint[blueprint.index(': ') + 2:]

    blueprint = blueprint.split('. ')
    blueprint = int(blueprint[0].split()[4]), int(blueprint[1].split()[4]), int(blueprint[2].split()[4]), int(blueprint[2].split()[7]), int(blueprint[3].split()[4]), int(blueprint[3].split()[7])
    blueprints.append(blueprint)

def can_buy(blueprint, resources):
    can_buy = []
    if resources[0] >= blueprint[0]: can_buy.append(0)
    if resources[0] >= blueprint[1]: can_buy.append(1)
    if resources[0] >= blueprint[2] and resources[1] >= blueprint[3]: can_buy.append(2)
    if resources[0] >= blueprint[4] and resources[2] >= blueprint[5]: can_buy.append(3)

    return can_buy

@cache
def minute(blueprint, robots, resources):
    robots = list(robots)
    resources = list(resources)
    outcomes = set()
    cb = can_buy(blueprint, resources)
    for r in range(4): resources[r] += robots[r]
    outcomes.add((tuple(robots), tuple(resources)))
    for r in cb:
        _robots = robots[:]
        _robots[r] += 1
        _resources = resources[:]
        if r == 0: _resources[0] -= blueprint[0]
        if r == 1: _resources[0] -= blueprint[1]
        if r == 2:
            _resources[0] -= blueprint[2]
            _resources[1] -= blueprint[3]
        if r == 3:
            _resources[0] -= blueprint[4]
            _resources[2] -= blueprint[5]
        outcomes.add((tuple(_robots), tuple(_resources)))
    return outcomes

def part1():
    s = 0
    for blueprint_id, blueprint in enumerate(blueprints):
        robots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]

        states = set([(tuple(robots), tuple(resources))])
        for m in range(24):
            new_states = set()
            for (robots, resources) in states:
                new_states |= minute(blueprint, tuple(robots), tuple(resources))

            states = set()
            max_vals = {}
            for robots, resources in new_states:
                if robots not in max_vals: max_vals[robots] = set([resources])
                else: max_vals[robots].add(resources)
            for robots, resources in new_states:
                if any(all(resources[r] <= r2[r] for r in range(4)) for r2 in max_vals[robots] if r2 != resources): continue
                for r in range(3):
                    if r == 0: max_cost = max(blueprint[0], blueprint[1], blueprint[2], blueprint[4])
                    elif r == 1: max_cost = blueprint[3]
                    else: max_cost  = blueprint[5]
                    deficit = max_cost - robots[r]
                    max_useful_qt = max_cost + deficit * (24 - m)
                    if resources[r] >= max_useful_qt:
                        rl = list(resources)
                        rl[r] = max_useful_qt
                        resources = tuple(rl)

                states.add((robots, resources))

        quality = (blueprint_id + 1) * max(state[1][3] for state in states)
        s += quality

    return s

def part2():
    s = 1
    for blueprint_id, blueprint in enumerate(blueprints[:3]):
        robots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]

        states = set([(tuple(robots), tuple(resources))])
        for m in range(32):
            new_states = set()
            for (robots, resources) in states:
                new_states |= minute(blueprint, tuple(robots), tuple(resources))

            states = set()
            max_vals = {}
            for robots, resources in new_states:
                if robots not in max_vals: max_vals[robots] = set([resources])
                else: max_vals[robots].add(resources)
            for robots, resources in new_states:
                if any(all(resources[r] <= r2[r] for r in range(4)) for r2 in max_vals[robots] if r2 != resources): continue
                for r in range(3):
                    if r == 0: max_cost = max(blueprint[0], blueprint[1], blueprint[2], blueprint[4])
                    elif r == 1: max_cost = blueprint[3]
                    else: max_cost  = blueprint[5]
                    deficit = max_cost - robots[r]
                    max_useful_qt = max_cost + deficit * (32 - m)
                    if resources[r] >= max_useful_qt:
                        rl = list(resources)
                        rl[r] = max_useful_qt
                        resources = tuple(rl)

                states.add((robots, resources))

        s *= max(state[1][3] for state in states)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
