from aoc import AOC

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
INCREASING_SEQS = [ALPHABET[i-2:i+1] for i in range(2, len(ALPHABET))]
FORBIDDEN = ['i', 'o', 'l']

aoc = AOC(11,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def elf_check(password):
    increasing = any([inc_seq in password for inc_seq in INCREASING_SEQS])
    non_forbidden = all([l not in password for l in FORBIDDEN])
    two_pairs = any([password[i] == password[i+1] and password[j] == password[j+1] for i in range(len(password) - 1) for j in range(i+2, len(password) - 1)])

    return increasing and non_forbidden and two_pairs

def increase(password):
    password = list(password)
    pos = len(password) - 1
    while True:
        i = ALPHABET.index(password[pos])

        if i < len(ALPHABET) - 1:
            password[pos] = ALPHABET[i + 1]
            return ''.join(password)
        else:
            password[pos] = ALPHABET[0]
            pos -= 1

def next_password(password):
    password = increase(password)
    while not elf_check(password):
        password = increase(password)

    return password

p1_sol = next_password(input[0])
p2_sol = next_password(p1_sol)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
