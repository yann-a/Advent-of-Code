from aoc import AOC

aoc = AOC(4,  2017, __file__)

input = aoc.input.strip().split('\n')

nb_valid = sum([all([word1 != word2 for i, word1 in enumerate(words) for j, word2 in enumerate(words) if i != j]) for passphrase in input if (words := passphrase.split())])
nb_valid2 = sum([all([set(word1) != set(word2) for i, word1 in enumerate(words) for j, word2 in enumerate(words) if i != j]) for passphrase in input if (words := passphrase.split())])

p1_sol = nb_valid
p2_sol = nb_valid2

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)