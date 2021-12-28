from aoc import AOC

aoc = AOC(9,  2016, __file__)

input = aoc.input.strip()

def decompressed_len(message):
    if '(' not in message:
        return len(message), len(message)
    
    first_o = message.index('(')
    first_c = message.index(')')

    pattern_len, nb_rep = map(int, message[first_o + 1: first_c].split('x'))
    pattern_dec_len = decompressed_len(message[first_c + 1: first_c + 1 + pattern_len])[1]

    next_dec_len = decompressed_len(message[first_c + 1 + pattern_len:])

    return first_o + pattern_len * nb_rep + next_dec_len[0], first_o + pattern_dec_len * nb_rep + next_dec_len[1]

p1_sol, p2_sol = decompressed_len(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
