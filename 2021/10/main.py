from aoc import AOC

aoc = AOC(10,  2021, __file__)

#input = aoc.get_example(1).split('\n')
input = aoc.input.split('\n')

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
rev_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2, '}': 3, '>': 4}

score1 = 0
score2_list = []

for k, line in enumerate(input):
    pile = []
    corrupted = False
    score2 = 0

    for c in line.strip():
        if c not in rev_pairs:
            pile.append(c)
        else:
            if pile[-1] == rev_pairs[c]:
                pile.pop(-1)
            else:
                # Line is corrupted, compute score and mark it as corrupted
                score1 += scores1[c]
                corrupted = True
                break

    # If line isn't corrupted, complete it and add the corresponding score to the list
    if not corrupted:
        for c in pile[::-1]:
            score2 *= 5
            score2 += scores2[pairs[c]]

        score2_list.append(score2)

p1_sol = score1
p2_sol = sorted(score2_list)[len(score2_list)//2]  # Median of the scores

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
