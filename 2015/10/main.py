from aoc import AOC

aoc = AOC(10,  2015, __file__)

input = [(3, 1), (1, 3), (3, 2), (2, 1), (1, 3)]

def step(previous):
    next = []

    for p in previous:
        if len(next) == 0:
            if p[0] == p[1]:
                next.append((2, p[0]))
            else:
                next.append((1, p[0]))
                next.append((1, p[1]))
        else:
            if p[0] == p[1]:
                if next[-1][1] == p[0]:
                    next[-1] = (next[-1][0] + 2, p[0])
                else:
                    next.append((2, p[0]))
            else:
                if next[-1][1] == p[0]:
                    next[-1] = (next[-1][0] + 1, p[0])
                    next.append((1, p[1]))
                else:
                    next.append((1, p[0]))
                    next.append((1, p[1]))

    return next

def len_apply(state, n):
    state = state[:]
    for _ in range(n):
        state = step(state)

    return sum([p[0] for p in state])

p1_sol = len_apply(input, 40)
p2_sol = len_apply(input, 50)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
