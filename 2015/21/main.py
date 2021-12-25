from aoc import AOC

aoc = AOC(21,  2015, __file__)

MAX_INT = 1_000_000

input = aoc.input.strip().split('\n')

# Add empty elements to acount for the fact that armors and rings are optional
WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMORS = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)] + [(0, 0, 0)]
RINGS = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)] + [(0, 0, 0), [0, 0, 0]]

boss_hp = int(input[0].split()[-1])
boss_damage = int(input[1].split()[-1])
boss_armor = int(input[2].split()[-1])

def win(hp, damage, armor):
    bhp = boss_hp
    bdamage = boss_damage
    barmor = boss_armor

    while True:
        bhp -= max(1, damage - barmor)
        if bhp <= 0:
            return True
        hp -= max(1, bdamage - armor)
        if hp <= 0:
            return False

minGoldToWin = MAX_INT
maxGoldToLose = 0
for weapon in WEAPONS:
    for armor in ARMORS:
        for i1, ring1 in enumerate(RINGS):
            for i2, ring2 in enumerate(RINGS):
                if i1 != i2:
                    cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                    damage_points = weapon[1] + armor[1] + ring1[1] + ring2[1]
                    armor_points = weapon[2] + armor[2] + ring1[2] + ring2[2]

                    if win(100, damage_points, armor_points):
                        minGoldToWin = min(minGoldToWin, cost)
                    else:
                        maxGoldToLose = max(maxGoldToLose, cost)

p1_sol = minGoldToWin
p2_sol = maxGoldToLose

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
