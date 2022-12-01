from aoc import AOC

aoc = AOC(16,  2017, __file__)

#input = aoc.get_example(0).strip()
input = aoc.input.strip()

seq = 'abcdefghijklmnop'
first_seq = None

# We get back to the initial config after 48 steps
for i in range(1_000_000_000 % 48):
    for instruction in input.split(','):
        if instruction[0] == 's':
            shift = int(instruction[1:])
            seq = seq[-shift:] + seq[:-shift]
        elif instruction[0] == 'x':
            a, b = map(int, instruction[1:].split('/'))
            a, b = min(a, b), max(a, b)

            seq = seq[:a] + seq[b] + seq[a + 1 : b] + seq[a] + seq[b + 1:]
        elif instruction[0] == 'p':
            a, b = instruction[1:].split('/')

            seq = seq.replace(a, '_').replace(b, a).replace('_', b)
    
    if first_seq is None:
        first_seq = seq

p1_sol = first_seq
p2_sol = seq

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
