from aoc import AOC
import re

aoc = AOC(19,  2020, __file__)

#input = aoc.get_example(2).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

# Read rules
rules = {}
for line in input[0].split('\n'):
    name, rep = line.split(': ')
    rep = rep.split(' | ')

    for r in rep:
        rules[name] = rules.get(name, []) + [r.split()]

# Generate regular expression
def gen_regex(rule, depth=25):
    if depth == 0:
        return ''
    
    if rule not in rules:
        return rule[1:-1]
    
    return '(' + '|'.join([''.join([gen_regex(el, depth-1) for el in alternative]) for alternative in rules[rule]]) + ')'

# Count matches
r = re.compile(gen_regex('0'))
p1_sol = sum([1 if r.fullmatch(msg) else 0 for msg in input[1].split("\n")])

# Update rules and recount matches
rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
r = re.compile(gen_regex('0'))
p2_sol = sum([1 if r.fullmatch(msg) else 0 for msg in input[1].split("\n")])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
