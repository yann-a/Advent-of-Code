from aoc import AOC
from collections import defaultdict

aoc = AOC(10,  2016, __file__)

input = aoc.input.strip().split('\n')

bot_op = {}
bot_chips = defaultdict(set)
outputs = defaultdict(int)

for line in input:
    line = line.split()

    if line[0] == 'value':
        bot_chips[int(line[-1])].add(int(line[1]))
    else:
        bot_op[int(line[1])] = (int(line[6]), line[5] == 'output', int(line[11]), line[10] == 'output')

comp_61_17 = None
while True:
    upd = False
    for bot in bot_op:
        if len(bot_chips[bot]) == 2:
            upd = True

            if 61 in bot_chips[bot] and 17 in bot_chips[bot]:
                comp_61_17 = bot
        
            low, low_output, high, high_output = bot_op[bot]
            if low_output:
                outputs[low] = min(bot_chips[bot])
            else:
                bot_chips[low].add(min(bot_chips[bot]))

            if high_output:
                outputs[high] = max(bot_chips[bot])
            else:
                bot_chips[high].add(max(bot_chips[bot]))

            bot_chips[bot] = set()

    if not upd:
        break

p1_sol = comp_61_17
p2_sol = outputs[0] * outputs[1] * outputs[2]

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
