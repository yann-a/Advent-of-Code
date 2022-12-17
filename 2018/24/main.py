from aoc import AOC
from collections import defaultdict

aoc = AOC(24,  2018, __file__)

input = list(map(lambda entry: entry.split('\n')[1:], aoc.input.strip().split('\n\n')))
#input = list(map(lambda entry: entry.split('\n')[1:], open('example', 'r').read().strip().split('\n\n')))

mapping = {'immune': 0, 'infection': 1}

def power(unit):
    return unit[1] * unit[3], unit[4]

def damage(attacker, defender):
    attack_power, _ = power(attacker)

    if attacker[5] in defender[6]['immune']: attack_power = 0
    elif attacker[5] in defender[6]['weak']: attack_power *= 2

    defeated_units = attack_power // defender[2]
    remaining_units = defender[1] - defeated_units

    return attack_power, max(remaining_units, 0)

def fight(boost=0):
    units = []
    remaining = defaultdict(int)
    for army in mapping:
        for line in input[mapping[army]]:
            precisions = line[line.index('(')+1:line.index(')')].split('; ') if '(' in line else []
            line = line.split()
            features = defaultdict(set)
            for precision in precisions:
                type = precision.split()[0]
                precision = precision[precision.index(' ', precision.index(' ') + 1) + 1:].split(', ')
                features[type] = set(precision)

            # army, nb, hp, attack_power, initiative, attack_type, features
            units.append([army, int(line[0]), int(line[4]), int(line[-6]) + (boost if army == 'immune' else 0), int(line[-1]), line[-5], features])
            remaining[army] += 1

    round = 1
    while True:
        # Target selection
        target_selection_order = sorted(list(range(len(units))), key=lambda unit_id: power(units[unit_id]), reverse=True)
        attacked = set()
        attacks = {}

        for attacker_id in range(len(units)):
            target_id, max_damage = -1, -1
            attacker_id = target_selection_order[attacker_id]
            for defender_id in range(len(units)):
                defender_id = target_selection_order[defender_id]
                if defender_id in attacked or units[attacker_id][0] == units[defender_id][0]: continue

                d = damage(units[attacker_id], units[defender_id])[0]
                if d > max_damage: target_id, max_damage = defender_id, d

                #print(f'{attacker_id} could attack {defender_id} with power {d}.')

            if target_id == -1 or max_damage <= 0: continue

            attacks[attacker_id] = target_id
            attacked.add(target_id)

            #print(f'{attacker_id} attacks {target_id} with power {max_damage}.')

        # Attack phase
        attacking_order = sorted(list(range(len(units))), key=lambda unit_id: units[unit_id][4], reverse=True)
        killed = set()
        damage_done = False
        for attacker_id in range(len(units)):
            attacker_id = attacking_order[attacker_id]

            if attacker_id not in attacks or attacker_id in killed: continue
            defender_id = attacks[attacker_id]

            attack_power, remaining_units = damage(units[attacker_id], units[defender_id])

            #print(f'{attacker_id} attacks {defender_id} with power {attack_power} and kills {units[defender_id][1] - remaining_units} units ({remaining_units} remaining).')

            if remaining_units != units[defender_id][1]:
                damage_done = True

            if remaining_units <= 0: killed.add(defender_id)
            units[defender_id][1] = remaining_units

        if not damage_done:
            return 0, None

        for unit_id in sorted(list(killed), reverse=True):
            remaining[units[unit_id][0]] -= 1
            units.pop(unit_id)

        if any(remaining[army] == 0 for army in remaining):
            break
    
    return sum(unit[1] for unit in units), units[0][0]

def part1():
    remaining_units, _ = fight()
    return remaining_units

def part2():
    boost = 0
    while True:
        remaining_units, winning_team = fight(boost)
        if winning_team == 'immune':
            return remaining_units
        boost += 1

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
