from aoc import AOC

aoc = AOC(5,  2023, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    seeds = list(map(int, input[0].split()[1:]))

    transformations = {}
    for transfo in input[1:]:
        lines = transfo.split('\n')

        name_line = lines[0].split()[0]
        name_tokens = name_line.split('-')
        source = name_tokens[0]
        destination = name_tokens[2]

        transformations[source] = [destination, {}]

        conv_lines = lines[1:]
        for line in conv_lines:
            dr, sr, rl = map(int, line.split())

            transformations[source][1][sr] = (dr, rl)

    min_location = 1_000_000_000
    for seed in seeds:
        p = seed
        p_name = 'seed'
        while p_name != 'location':
            t = transformations[p_name]

            p_name = t[0]
            for sr in t[1]:
                dr, rl = t[1][sr]
                if sr <= p < sr + rl:
                    p = p + (dr - sr)
                    break

        min_location = min(min_location, p)

    return min_location

def part2():
    seeds = list(map(int, input[0].split()[1:]))

    transformations = {}
    for transfo in input[1:]:
        lines = transfo.split('\n')

        name_line = lines[0].split()[0]
        name_tokens = name_line.split('-')
        source = name_tokens[0]
        destination = name_tokens[2]

        transformations[source] = [destination, {}]

        conv_lines = lines[1:]
        for line in conv_lines:
            dr, sr, rl = map(int, line.split())

            transformations[source][1][sr] = (dr, rl)

    p = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    p_name = 'seed'
    while p_name != 'location':
        t = transformations[p_name]

        p_name = t[0]
        new_p = []
        for sr in t[1]:
            dr, rl = t[1][sr]
            cp = []
            for (s, r) in p:
                if s + r - 1 >= sr and s <= sr + rl - 1:
                    low_end = max(sr, s) + (dr - sr)
                    high_end = min(sr + rl - 1, s + r - 1) + (dr - sr)
                    new_p.append((low_end, high_end - low_end + 1))
                    if s < sr:
                        cp.append((s, sr - s))
                    if s + r - 1 > sr + rl - 1:
                        cp.append((sr + rl - 1, s + r - 1 - (sr + rl - 1)))
                else:
                    cp.append((s, r))
            p = cp
        p = p + new_p

    return min([e[0] for e in p])

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)