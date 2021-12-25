from aoc import AOC
from queue import PriorityQueue

aoc = AOC(22,  2015, __file__)

input = aoc.input.strip().split('\n')

SPELLS_COST = [53, 73, 113, 173, 229]

bhp = int(input[0].split()[-1])
boss_damage = int(input[1].split()[-1])

def solve(part=1):
    queue = PriorityQueue()
    queue.put((0, True, 50, 500, bhp, 0, 0, 0)) # Spent mana, turn, hp, mana, boss hp, counters for shield, poison and recharge

    while not queue.empty():
        spent, turn, hp, mana, boss_hp, sc, pc, rc = queue.get()

        if boss_hp <= 0:
            return spent

        armor = 7 if sc > 0 else 0
        if pc > 0: boss_hp -= 3
        if rc > 0: mana += 101

        if not turn:
            new_hp = hp - max(1, boss_damage - armor)
            if new_hp > 0:
                queue.put((spent, True, new_hp, mana, boss_hp, max(0, sc - 1), max(0, pc - 1), max(0, rc - 1)))
        else:
            if part == 2:
                hp -= 1
                if hp <= 0:
                    continue
                    
            for spell_id, cost in enumerate(SPELLS_COST):
                if mana >= cost:
                    if spell_id == 0:
                        queue.put((spent + cost, False, hp, mana - cost, boss_hp - 4, max(0, sc - 1), max(0, pc - 1), max(0, rc - 1)))
                    elif spell_id == 1:
                        queue.put((spent + cost, False, hp + 2, mana - cost, boss_hp - 2, max(0, sc - 1), max(0, pc - 1), max(0, rc - 1)))
                    elif spell_id == 2:
                        queue.put((spent + cost, False, hp, mana - cost, boss_hp, 6, max(0, pc - 1), max(0, rc - 1)))
                    elif spell_id == 3:
                        queue.put((spent + cost, False, hp, mana - cost, boss_hp, max(0, sc - 1), 6, max(0, rc - 1)))
                    else:
                        queue.put((spent + cost, False, hp, mana - cost, boss_hp, max(0, sc - 1), max(0, pc - 1), 5))

p1_sol = solve()
p2_sol = solve(2)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
