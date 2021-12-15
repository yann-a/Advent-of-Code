depths = [int(line) for line in open('input', 'r')]


def solve(shift):
    increased = 0
    for i in range(shift, len(depths)):
        if depths[i-shift] < depths[i]:
            increased += 1

    return increased


print('Part 1:', solve(1))
print('Part 2:', solve(3))
