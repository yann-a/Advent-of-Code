from aoc import AOC

aoc = AOC(7,  2016, __file__)

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

input = aoc.input.strip().split('\n')

abbas = [f'{a}{b}{b}{a}' for a in ALPHABET for b in ALPHABET if a != b]
abas = {f'{a}{b}{a}': f'{b}{a}{b}' for a in ALPHABET for b in ALPHABET if a != b}

nb_tls = nb_ssl = 0
for line in input:
    chunks = line.split('[')

    outside_brackets = [chunks[0]] + [chunk.split(']')[1] for chunk in chunks[1:]]
    inside_brackets = [chunk.split(']')[0] for chunk in chunks[1:]]

    if any([abba in outside for abba in abbas for outside in outside_brackets]) and \
        all([abba not in inside for abba in abbas for inside in inside_brackets]):
        nb_tls += 1
    
    if any([aba in outside and abas[aba] in inside for aba in abas for outside in outside_brackets for inside in inside_brackets]):
        nb_ssl += 1

p1_sol = nb_tls
p2_sol = nb_ssl

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
