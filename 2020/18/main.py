from aoc import AOC

aoc = AOC(18,  2020, __file__)

input = aoc.get_example(1).strip().split('\n')
input = """
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip().split('\n')
input = aoc.input.strip().split('\n')

def eval1(tokens):
    nbP, level0Ops = 0, []
    for k, token in enumerate(tokens):
        for c in token:
            if c == '(': nbP += 1
            if c == ')': nbP -= 1 
        if token in ['+', '*'] and nbP == 0:
            level0Ops.append(k)

    if len(level0Ops) == 0:
        if len(tokens) == 1: return int(tokens[0])
        else: return eval1([tokens[0][1:]] + tokens[1:-1] + [tokens[-1][:-1]])

    n = len(level0Ops)
    parts = [eval1(tokens[:level0Ops[0]])] + [eval1(tokens[level0Ops[i] + 1:level0Ops[i+1]]) for i in range(0, n-1)] + [eval1(tokens[level0Ops[n-1] + 1:])]

    acc = parts[0]
    for k, op in enumerate(level0Ops):
        if tokens[op] == '+': acc += parts[k + 1]
        elif tokens[op] == '*': acc *= parts[k + 1]

    return acc

def eval2(tokens):
    nbP, level0Plus, level0Mult = 0, [], []
    for k, token in enumerate(tokens):
        for c in token:
            if c == '(': nbP += 1
            if c == ')': nbP -= 1 
        if token == '+' and nbP == 0:
            level0Plus.append(k)
        elif token == '*' and nbP == 0:
            level0Mult.append(k)

    if len(level0Mult) > 0:
        nMults = len(level0Mult)
        multParts = [eval2(tokens[:level0Mult[0]])] + [eval2(tokens[level0Mult[i] + 1:level0Mult[i+1]]) for i in range(0, nMults-1)] + [eval2(tokens[level0Mult[nMults-1] + 1:])]

        acc = 1
        for p in multParts: acc *= p

        return acc
    elif len(level0Plus) > 0:
        nPlus = len(level0Plus)

        plusParts = [eval2(tokens[:level0Plus[0]])] + [eval2(tokens[level0Plus[i] + 1:level0Plus[i+1]]) for i in range(0, nPlus-1)] + [eval2(tokens[level0Plus[nPlus-1] + 1:])]

        acc = 0
        for p in plusParts: acc += p

        return acc
    else:
        if len(tokens) == 1: return int(tokens[0])
        else: return eval2([tokens[0][1:]] + tokens[1:-1] + [tokens[-1][:-1]])

p1_sol = sum([eval1(line.split()) for line in input])
p2_sol = sum([eval2(line.split()) for line in input])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
