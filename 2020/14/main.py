from aoc import AOC

aoc = AOC(14,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

# Part 1
mem = {}
for instruction in input:
    if instruction[1] == 'a':
        mask = instruction.split(' = ')[1]
        mask0 = int(''.join(['0' if c == '0' else '1' for c in mask]), base=2)
        mask1 = int(''.join(['1' if c == '1' else '0' for c in mask]), base=2)
    else:
        dest, val = instruction.split(' = ')
        dest, val = int(dest[4:-1]), int(val)

        mem[dest] = (val & mask0 | mask1)

p1_sol = sum(mem.values())

# Part 2
mem = {}
for instruction in input:
    if instruction[1] == 'a':
        mask = instruction.split(' = ')[1]
        mask1 = int(''.join(['1' if c == '1' else '0' for c in mask]), base=2)
        Xpos = [i for i, c in enumerate(mask) if c == 'X']
    else:
        dest, val = instruction.split(' = ')
        dest, val = str(bin((int(dest[4:-1]) | mask1))), int(val)
        dest = '0' * (38 - len(dest)) + dest[2:]

        for i in range(2 ** len(Xpos)):
            new_dest = dest
            for j, k in enumerate(Xpos):
                new_dest = new_dest[:k] + ('1' if ((i >> j) & 1) != 0 else '0') + new_dest[k + 1:]

            new_dest = int(new_dest, base=2)
            mem[new_dest] = val

p2_sol = sum(mem.values())

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
