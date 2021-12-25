from aoc import AOC

aoc = AOC(7,  2015, __file__)

input = aoc.input.strip().split('\n')

circuit = {}
for instruction in input:
    inst, output = instruction.split(' -> ')

    if len(inst.split(' AND ')) == 2:
        circuit[output] = ('and', inst.split(' AND ')[0], inst.split(' AND ')[1])
    elif len(inst.split(' OR ')) == 2:
        circuit[output] = ('or', inst.split(' OR ')[0], inst.split(' OR ')[1])
    elif len(inst.split(' LSHIFT ')) == 2:
        circuit[output] = ('lshift', inst.split(' LSHIFT ')[0], inst.split(' LSHIFT ')[1])
    elif len(inst.split(' RSHIFT ')) == 2:
        circuit[output] = ('rshift', inst.split(' RSHIFT ')[0], inst.split(' RSHIFT ')[1])
    elif len(inst.split('NOT ')) == 2:
        circuit[output] = ('not', inst.split('NOT ')[1])
    else:
        circuit[output] = ('single', inst)

def solve(value, values={}):
    values = values.copy()
    def resolve(value):
        if value in values:
            return values[value]
        
        try:
            return int(value)
        except:
            pass

        if circuit[value][0] == 'and':
            res = resolve(circuit[value][1]) & resolve(circuit[value][2])
        elif circuit[value][0] == 'or':
            res = resolve(circuit[value][1]) | resolve(circuit[value][2])
        elif circuit[value][0] == 'lshift':
            res = resolve(circuit[value][1]) << resolve(circuit[value][2])
        elif circuit[value][0] == 'rshift':
            res = resolve(circuit[value][1]) >> resolve(circuit[value][2])
        elif circuit[value][0] == 'not':
            res = ~resolve(circuit[value][1])
        else:
            res = resolve(circuit[value][1])

        values[value] = res
        return res

    return resolve(value)

p1_sol = solve('a')
p2_sol = solve('a', {'b': p1_sol})

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
