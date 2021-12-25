from aoc import AOC

aoc = AOC(25,  2015, __file__)

FIRST_ELEM = 20151125
MULT_FACT = 252533
MODULO = 33554393

input = aoc.input.strip().split('\n')

row = int(input[0].split()[-3][:-1])
col = int(input[0].split()[-1][:-1])

diag_id = row + col - 1
start_diag_nb = diag_id * (diag_id - 1) // 2 + 1
element_nb = start_diag_nb + col - 1

element = (FIRST_ELEM * pow(MULT_FACT, element_nb - 1, MODULO)) % MODULO

p1_sol = element

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
