from aoc import AOC
from collections import defaultdict

aoc = AOC(4,  2018, __file__)

input = aoc.input.strip().split('\n')
input.sort()
#input = aoc.get_example(0).strip().split('\n')

def part1():
    asleep_time = defaultdict(int)
    last_asleep = current_guard = 0

    for entry in input:
        date = entry[1:17].split()
        action = entry[19:].split()

        if action[0] == 'Guard':
            current_guard = action[1][1:]
        elif action[0] == 'wakes':
            asleep_time[current_guard] += int(date[1][-2:]) - last_asleep
        else:
            last_asleep = int(date[1][-2:])

    most_asleep_guard = max([(asleep_time[id], id) for id in asleep_time])[1]
    sleeped_minutes = defaultdict(int)
    
    for entry in input:
        date = entry[1:17].split()
        action = entry[19:].split()

        if action[0] == 'Guard':
            current_guard = action[1][1:]
        elif action[0] == 'wakes':
            if current_guard == most_asleep_guard:
                for minute in range(last_asleep, int(date[1][-2:])):
                    sleeped_minutes[minute] += 1
        else:
            last_asleep = int(date[1][-2:])

    most_sleeped_minute = max([(sleeped_minutes[m], m) for m in sleeped_minutes])[1]

    return int(most_asleep_guard) * most_sleeped_minute

def part2():
    asleep_time = defaultdict(int)
    last_asleep = current_guard = 0

    for entry in input:
        date = entry[1:17].split()
        action = entry[19:].split()

        if action[0] == 'Guard':
            current_guard = action[1][1:]
        elif action[0] == 'wakes':
            for minute in range(last_asleep, int(date[1][-2:])):
                asleep_time[(current_guard, minute)] += 1
        else:
            last_asleep = int(date[1][-2:])

    _, guard, m = max([(asleep_time[(guard, m)], guard, m) for (guard, m) in asleep_time])

    return int(guard) * m

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
