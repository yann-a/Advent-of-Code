from aoc import AOC

aoc = AOC(2,  2015, __file__)

input = aoc.input.strip().split('\n')

paper_area = 0
ribon_length = 0
for gift in input:
    l, L, h = map(int, gift.split('x'))

    paper_area += 2*(l*L + l*h + L*h) + min(l*L, l*h, L*h)
    ribon_length += 2*min(l+L, l+h, L+h) + l*L*h

p1_sol = paper_area
p2_sol = ribon_length

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
