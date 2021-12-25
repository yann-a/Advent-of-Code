from aoc import AOC

aoc = AOC(15,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

ingredients = []
for line in input:
    line = line.split()
    ingredients.append((int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])))

max_score = 0
max_score_500 = 0
for c1 in range(100):
    for c2 in range(100 - c1):
        for c3 in range(100 - c1 - c2):
            c4 = 100 - c1 - c2 - c3

            scores = [c1 * ingredients[0][i] + c2 * ingredients[1][i] + c3 * ingredients[2][i] + c4 * ingredients[3][i] for i in range(5)]

            total_score = 1
            for s in scores[:-1]:
                total_score *= max(0, s)
            
            max_score = max(max_score, total_score)
            if scores[-1] == 500:
                max_score_500 = max(max_score_500, total_score)

p1_sol = max_score
p2_sol = max_score_500

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
