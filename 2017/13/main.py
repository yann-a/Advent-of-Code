from aoc import AOC

aoc = AOC(13,  2017, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

layers = {int(l[0]): int(l[1]) for line in input if (l := line.split(': '))}

def get_severity(delay=0):
    severity = 0
    caught = False
    for depth in layers:
        r = layers[depth]
        if (depth + delay) % (2 * (r - 1)) == 0:
            caught = True
            severity += depth * r

    return severity, caught

p1_sol = get_severity()[0]

delay = 0
while get_severity(delay)[1]:
    delay += 1
p2_sol = delay

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
