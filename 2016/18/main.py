from aoc import AOC

aoc = AOC(18,  2016, __file__)

input = aoc.input.strip()

TRAP_NEIGHBORHOOD = [('^', '^', '.'), ('.', '^', '^'), ('.', '.', '^'), ('^', '.', '.')]

def neighborhood(row, index):
    prev = row[index - 1] if index > 0 else '.'
    next = row[index + 1] if index < len(row) - 1 else '.'

    return prev, row[index], next

def step(row):
    return ''.join(['^' if neighborhood(row, index) in TRAP_NEIGHBORHOOD else '.' for index in range(len(row))])

row = input
nb_safe_40 = None
nb_safe = sum([tile == '.' for tile in row])
for i in range(1, 400_000):
    if i == 40:
        nb_safe_40 = nb_safe
    row = step(row)
    nb_safe += sum([tile == '.' for tile in row])

p1_sol = nb_safe_40
p2_sol = nb_safe

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
