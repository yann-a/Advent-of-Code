from aoc import AOC

aoc = AOC(5,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = """
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
FBFBBFFRLR
""".strip().split('\n')
input = aoc.input.strip().split('\n')

ids = []
for seat in input:
    binary_row = ''.join(['0' if c == 'F' else '1' for c in seat[:7]])
    row = int(binary_row, base=2)

    binary_col = ''.join(['0' if c == 'L' else '1' for c in seat[-3:]])
    col = int(binary_col, base=2)

    ids.append(row * 8 + col)

p1_sol = max(ids)
i = min(ids) + 1
while i in ids:
    i += 1
p2_sol = i

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
