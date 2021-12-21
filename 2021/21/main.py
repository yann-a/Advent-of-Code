from aoc import AOC
import sys
sys.setrecursionlimit(1_000_000)

aoc = AOC(21,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

pos_1, pos_2 = int(input[0].split()[-1]), int(input[1].split()[-1])

def part1(pos_1, pos_2):
    score_1 = score_2 = 0
    dice_next, rolls = 1, 0

    def draw(dice_next, n=3):
        adv = 0
        for _ in range(n):
            adv += dice_next
            dice_next += 1
            if dice_next == 101:
                dice_next = 1

        return adv, dice_next, rolls + n

    while score_1 < 1000 and score_2 < 1000:
        adv, dice_next, rolls = draw(dice_next)
        pos_1 += adv 
        pos_1 = (pos_1 - 1) % 10 + 1

        score_1 += pos_1
        if score_1 >= 1000:
            break

        adv, dice_next, rolls = draw(dice_next)
        pos_2 += adv 
        pos_2 = (pos_2 - 1) % 10 + 1

        score_2 += pos_2

    return rolls * min(score_1, score_2)

def part2(pos_1, pos_2):
    # DP. read mem[node][s2][s1][p2][p1][turn] as the number of universes there is in which 'node' wins, starting from
    # the state where player i has a score si and is at position pi + 1; and it is player `turn + 1`'s turn to play
    dices_sums = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
    mem = [[[[[[0 for _ in range(2)] for _ in range(10)] for _ in range(10)] for _ in range(22)] for _ in range(22)] for _ in range(2)]

    for s1 in range(21, -1, -1):
        for s2 in range(21, -1, -1):
            for p1 in range(10):
                for p2 in range(10):
                    for node in range(2):
                        for turn in range(2):
                            if s1 == 21:
                                mem[node][s2][s1][p2][p1][turn] = node == 0
                            elif s2 == 21:
                                mem[node][s2][s1][p2][p1][turn] = node == 1
                            else:
                                if turn == 0:
                                    for dices_sum, count in dices_sums:
                                        new_p1 = (p1 + dices_sum) % 10
                                        mem[node][s2][s1][p2][p1][turn] += count * mem[node][s2][min(21, s1 + new_p1 + 1)][p2][new_p1][1 - turn]
                                else:
                                    for dices_sum, count in dices_sums:
                                        new_p2 = (p2 + dices_sum) % 10
                                        mem[node][s2][s1][p2][p1][turn] += count * mem[node][min(21, s2 + new_p2 + 1)][s1][new_p2][p1][1 - turn]

    waysToWin1 = mem[0][0][0][pos_2 - 1][pos_1 - 1][0]
    waysToWin2 = mem[1][0][0][pos_2 - 1][pos_1 - 1][0]

    return max(waysToWin1, waysToWin2)
        
p1_sol = part1(pos_1, pos_2)
p2_sol = part2(pos_1, pos_2)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
