init_clocks = {x: 0 for x in range(9)}
for clock in open('input').readline().split(','):
    init_clocks[int(clock)] += 1


def simulate_growth(days):
    clocks = init_clocks.copy()

    for day in range(days):
        new_clocks = {x: 0 for x in range(9)}

        for c in range(1, 9):
            new_clocks[c - 1] = clocks[c]
        new_clocks[8] = clocks[0]
        new_clocks[6] += clocks[0]

        clocks = new_clocks

    return sum([clocks[i] for i in range(9)])


print('Part 1:', simulate_growth(80))
print('Part 2:', simulate_growth(256))
