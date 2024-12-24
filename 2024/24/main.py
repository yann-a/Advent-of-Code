from aoc import AOC
from collections import defaultdict
from itertools import combinations

aoc = AOC(24,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    values = defaultdict(int)
    for line in input[0].split('\n'):
        values[line[:3]] = int(line.split()[1])

    relations = {}
    for line in input[1].split('\n'):
        line = line.split()
        relations[line[-1]] = (line[1], line[0], line[2])

    def get_value(var):
        if var in values:
            return values[var]
        else:
            rel = relations[var]
            if rel[0] == 'AND':
                values[var] = get_value(rel[1]) & get_value(rel[2])
            elif rel[0] == 'OR':
                values[var] = get_value(rel[1]) | get_value(rel[2])
            elif rel[0] == 'XOR':
                values[var] = get_value(rel[1]) ^ get_value(rel[2])

            return values[var]

    for v in relations:
        get_value(v)

    z_keys = [k for k in relations.keys() if k[0] == 'z']
    z_keys.sort(reverse=True)

    s = ''
    for z_k in z_keys:
        s += str(values[z_k])

    return int(s, 2)

def part2():
    # No nice automatic solution for part 2 today. I analyzed the structure of each step of the full adder.
    # This step checks the structure it expects, keeping the name of the carry variable, and when it detects an anomaly
    # it crashes, then I fix the input manually and I start again until everything is fixed
    # Each step looks like this
    #
    # ntt OR spq -> ndd
    # gnj AND jfw -> spq
    # x01 AND y01 -> ntt
    # y01 XOR x01 -> gnj
    # jfw XOR gnj -> z01
    #
    # where jfw is the carry from the previous step, and ndd is the carry passed on to the next step

    input = open('input_fixed').read().strip().split('\n\n')

    values = defaultdict(int)
    for line in input[0].split('\n'):
        values[line[:3]] = int(line.split()[1])

    relations = {}
    for line in input[1].split('\n'):
        line = line.split()
        relations[line[-1]] = (line[1], line[0], line[2])

    insts = {}
    insts[0] = [('z00', 'XOR', 'x00', 'y00'), ('jfw', 'AND', 'x00', 'y00')]
    carry_name = 'jfw'
    for z in range(1, 45):
        print(z, carry_name)
        insts_ = []

        i1 = list(relations[f'z{z:02}'])
        assert i1[0] == 'XOR'
        if i1[1] == carry_name:
            pass
        elif i1[2] == carry_name:
            i1[1], i1[2] = i1[2], i1[1]
        else:
            assert 1 == 0
        insts_.append((f'z{z:02}', 'XOR', i1[1], i1[2]))

        i2 = relations[i1[2]]
        assert i2[0] == 'XOR'
        assert (i2[1] == f'x{z:02}' and i2[2] == f'y{z:02}') or (i2[2] == f'x{z:02}' and i2[1] == f'y{z:02}')
        insts_.append((i1[2], 'XOR', i2[1], i2[2]))

        next_inst = [rel for rel in relations if relations[rel][0] == 'AND' and set([relations[rel][1], relations[rel][2]]) == set([f'x{z:02}', f'y{z:02}'])][0]
        i3 = relations[next_inst]
        insts_.append((next_inst, 'AND', i3[1], i3[2]))
        
        next_inst2 = [rel for rel in relations if relations[rel][0] == 'OR' and next_inst in set([relations[rel][1], relations[rel][2]])][0]
        i4 = relations[next_inst2]
        insts_.append((next_inst2, 'OR', i4[1], i4[2]))

        next_inst3 = tuple(set([i4[1], i4[2]]) - set(next_inst))[0]
        i5 = relations[next_inst3]
        assert i5[0] == 'AND'
        insts_.append((next_inst3, 'AND', i5[1], i5[2]))

        carry_name = next_inst2
        insts[z] = insts_

    # Manually filled in
    swaped_wires = ['hbk', 'z14', 'kvn', 'z18', 'dbb', 'z23', 'tfn', 'cvh']
    return ','.join(sorted(swaped_wires))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
