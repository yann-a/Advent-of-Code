report = [l.strip() for l in open('input')]
l = len(report[0])


def maj(elements, index, min=False):
    nb = [0, 0]
    for el in elements:
        nb[int(el[index])] += 1

    if nb[0] > nb[1]:
        return '1' if min else '0'
    else:
        return '0' if min else '1'


# Part 1
gamma = ''.join([maj(report, i) for i in range(l)])
epsilon = ''.join([maj(report, i, True) for i in range(l)])

print('Part 1:', int(gamma, 2) * int(epsilon, 2))

# Part 2
oxygen, co2 = report, report
for i in range(l):
    if len(oxygen) > 1:
        oxygen = [el for el in oxygen if el[i] == maj(oxygen, i)]
    if len(co2) > 1:
        co2 = [el for el in co2 if el[i] == maj(co2, i, True)]

print('Part 2:', int(oxygen[0], 2) * int(co2[0], 2))
