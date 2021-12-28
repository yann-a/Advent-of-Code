from aoc import AOC

aoc = AOC(3,  2016, __file__)

input = aoc.input.strip().split('\n')

def count_triangles(triplets):
    possible = 0
    for a, b, c in triplets:
        if max(a, b, c) < (a + b + c)/2:
            possible += 1

    return possible

p1_sol = count_triangles(list(map(lambda line: map(int, line.split()), input)))
p2_sol = count_triangles([map(int, [input[row + drow].split()[col] for drow in range(3)]) for col in range(3) for row in range(0, len(input), 3)])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
