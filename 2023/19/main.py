from aoc import AOC

aoc = AOC(19,  2023, __file__)

input = aoc.input.strip().split('\n\n')
#input = open('example', 'r').read().strip().split('\n\n')

def processpart(workflows, part):
    process = 'in'
    while True:
        for rule in workflows[process]:
            if len(rule) == 1:
                if rule[0] == 'A': return True
                elif rule[0] == 'R': return False
                else:
                    process = rule[0]
                    break
            else:
                if (rule[0][1] == '<' and part[rule[0][0]] < int(rule[0][2:])) or (rule[0][1] == '>' and part[rule[0][0]] > int(rule[0][2:])):
                    if rule[1] == 'A': return True
                    elif rule[1] == 'R': return False
                    else:
                        process = rule[1]
                        break

def part1():
    workflows_ = input[0].split('\n')
    workflows = {}
    for workflow in workflows_:
        name = workflow[:workflow.index('{')]
        process = workflow[workflow.index('{') + 1:-1]
        rules = process.split(',')
        rules = [rule.split(':') for rule in rules]

        workflows[name] = rules

    s = 0
    parts = input[1].split('\n')
    for part_ in parts:
        part = {c[0]: int(c[2:]) for c in part_[1:-1].split(',')}
        if processpart(workflows, part):
            s += sum(part.values())

    return s

def nbcomb(r):
    s = 1
    for n in 'xmas':
        s *= r[n][1] - r[n][0] + 1

    assert(s > 0)

    return s

def nbaccept(workflows, name, r):
    s = 0
    cr = {l: r[l][:] for l in r}
    for rule in workflows[name]:
        if len(rule) == 1:
            if rule[0] == 'A': s += nbcomb(cr)
            elif rule[0] == 'R': pass
            else: s += nbaccept(workflows, rule[0], cr)
        else:
            v, op, val = rule[0][0], rule[0][1], int(rule[0][2:])
            if (op == '<' and cr[v][0] < val) or (op == '>' and cr[v][1] > val):
                nr = {l: cr[l][:] for l in cr}

                if op == '<': nr[v][1] = min(val - 1, nr[v][1])
                else: nr[v][0] = max(val + 1, nr[v][0])

                if rule[1] == 'A': s += nbcomb(nr)
                elif rule[1] == 'R': pass
                else: s += nbaccept(workflows, rule[1], nr)

                if op == '<' and val - 1 < cr[v][1]: cr[v][0] = val
                elif op == '>' and val + 1 > cr[v][0]: cr[v][1] = val
                else: break

    return s

def part2():
    workflows_ = input[0].split('\n')
    workflows = {}
    for workflow in workflows_:
        name = workflow[:workflow.index('{')]
        process = workflow[workflow.index('{') + 1:-1]
        rules = process.split(',')
        rules = [rule.split(':') for rule in rules]

        workflows[name] = rules

    return nbaccept(workflows, 'in', {'x':[1, 4_000], 'm':[1, 4_000], 'a':[1, 4_000], 's':[1, 4_000]})

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
