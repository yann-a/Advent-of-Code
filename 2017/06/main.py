from aoc import AOC

aoc = AOC(6,  2017, __file__)

input = list(map(int, aoc.input.strip().split()))

def serialize(config):
    return '_'.join(map(str, config))

def deserialize(config):
    return list(map(int, config.split('_')))

config = input[:]

seen = {}
steps = 0
while not serialize(config) in seen:
    seen[serialize(config)] = steps

    redistrib = config.index(max(config))
    nb_redistrib = max(config)
    config[redistrib] = 0

    while nb_redistrib > 0:
        redistrib  = (redistrib + 1) % len(config)
        config[redistrib] += 1
        nb_redistrib -= 1

    steps += 1

p1_sol = steps
p2_sol = steps - seen[serialize(config)]

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)