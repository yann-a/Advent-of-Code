from aoc import AOC
from functools import reduce

aoc = AOC(16,  2021, __file__)

#input = aoc.get_example(3).strip().split('\n')
input = aoc.input.strip().split('\n')

def red_fun(t):
    if t == 0: return (lambda x, y: x + y)
    if t == 1: return (lambda x, y: x * y)
    if t == 2: return (lambda x, y: min(x, y))
    if t == 3: return (lambda x, y: max(x, y))
    if t == 5: return (lambda x, y: 1 if x > y else 0)
    if t == 6: return (lambda x, y: 1 if x < y else 0)
    if t == 7: return (lambda x, y: 1 if x == y else 0)

def read(packet):
    """
        input:  a string starting with a packet, ans possibly more data
        output: the first packet in the string, number of consumed bits, rest of the string, sum of version ids
    """
    v, packet = int(packet[:3], base=2), packet[3:]
    t, packet = int(packet[:3], base=2), packet[3:]

    if t == 4:
        # literal value
        lit_bin = ''
        consumed_bits = 6

        while True:
            part, packet = packet[:5], packet[5:]

            lit_bin += part[1:]
            consumed_bits += 5

            if part[0] == '0':
                break
        
        return int(lit_bin, base=2), consumed_bits, packet, v
    else:
        # operator value
        i, packet = int(packet[:1], base=2), packet[1:]

        consumed_bits = 7

        if i == 0: l, packet, consumed_bits = int(packet[:15], base=2), packet[15:], consumed_bits + 15
        else:      l, packet, consumed_bits = int(packet[:11], base=2), packet[11:], consumed_bits + 11

        values = []
        read_bits, inner_vs = 0, 0
        while (i == 0 and read_bits < l) or (i == 1 and len(values) < l):
            value, cons, packet, inner_v = read(packet)

            values.append(value)
            read_bits += cons
            consumed_bits += cons
            inner_vs += inner_v

        return reduce(red_fun(t), values), consumed_bits, packet, v + inner_vs

p2_sol, _, _, p1_sol = read(bin(int(input[0], base=16))[2:])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
