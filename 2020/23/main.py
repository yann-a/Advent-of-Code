from aoc import AOC

aoc = AOC(23,  2020, __file__)

input = "389125467"
input = "398254716"

NB_CUPS = 1_000_000
NB_STEPS = 10_000_000

def step(cups):
    selected = [cups[1], cups[2], cups[3]]

    destination = cups[0] - 1 if cups[0] - 1 >= min(cups) else max(cups)
    while destination not in set(cups) - set(selected):
        destination = destination - 1 if destination - 1 >= min(cups) else max(cups)

    pos_dest = cups.index(destination)
    cups = cups[4:pos_dest] + [destination] + selected + cups[pos_dest + 1:] + [cups[0]]

    return cups

def stepDicts(cups, current):
    selected = []
    for _ in range(3):
        selected.append(cups[current])
        cups[current] = cups[cups[current]]

    destination = current - 1 if current - 1 >= 1 else NB_CUPS
    while destination in selected:
        destination = destination - 1 if destination - 1 >= 1 else NB_CUPS

    cups[selected[2]] = cups[destination]
    cups[selected[1]] = selected[2]
    cups[selected[0]] = selected[1]
    cups[destination] = selected[0]

    return cups, cups[current]

def part1(cups_string):
    cups = list(map(int, list(cups_string)))
    for _ in range(100):
        cups = step(cups)

    index_1 = cups.index(1)
    return ''.join(map(str, cups[index_1 + 1:] + cups[:index_1]))

def part2(cups_string):
    cups = {int(cups_string[i]): int(cups_string[i+1]) for i in range(len(cups_string) - 1)}
    cups[int(cups_string[-1])] = len(cups_string) + 1
    for i in range(len(cups_string) + 1, NB_CUPS):
        cups[i] = i + 1
    cups[NB_CUPS] = int(cups_string[0])

    current = int(cups_string[0])
    for _ in range(NB_STEPS):
        cups, current = stepDicts(cups, current)

    return cups[1] * cups[cups[1]]

p1_sol = part1(input)
p2_sol = part2(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
