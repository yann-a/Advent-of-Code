from aoc import AOC
from functools import reduce

aoc = AOC(16,  2020, __file__)

input = aoc.get_example(2).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

validity = {}
for row in input[0].split('\n'):
    name, vals = row.split(': ')
    i1, i2 = vals.split(' or ')
    i11, i12 = list(map(int, i1.split('-')))
    i21, i22 = list(map(int, i2.split('-')))

    validity[name] = ((i11, i12), (i21, i22))

p1_sol = 0
tickets = [list(map(int, input[1].split('\n')[1].split(',')))]
for ticket in input[2].split('\n')[1:]:
    isTicketOk = True
    ticket = list(map(int, ticket.split(',')))

    for v in ticket:
        isValOk = False

        for name in validity:
            ((i11, i12), (i21, i22)) = validity[name]
            if (i11 <= v <= i12) or (i21 <= v <= i22):
                isValOk = True

        if not isValOk:
            isTicketOk = False
            p1_sol += v
    
    if isTicketOk:
        tickets.append(ticket)

fields_can_be = {name: set(range(len(tickets[0]))) for name in validity}
for ticket in tickets:
    for i, v in enumerate(ticket):
        for name in validity:
            ((i11, i12), (i21, i22)) = validity[name]
            if not((i11 <= v <= i12) or (i21 <= v <= i22)):
                fields_can_be[name] = fields_can_be[name].difference(set([i]))
mapping = {}
while len(mapping) < len(tickets[0]):
    for name in fields_can_be:
        if len(fields_can_be[name]) == 1:
            mapping[name] = list(fields_can_be[name])[0]
            for name2 in fields_can_be:
                fields_can_be[name2] = fields_can_be[name2].difference(set([mapping[name]]))

p2_sol = reduce(lambda x, y: x * y, [tickets[0][mapping[k]] for k in mapping if k.startswith('departure')])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
