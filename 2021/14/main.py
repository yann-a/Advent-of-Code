from aoc import AOC

aoc = AOC(14,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

template = input[0]
# Dict pairs -> nb of occurences
pairs = {}
for i in range(1, len(template)):
    pairs[template[i-1:i+1]] = pairs.get(template[i-1:i+1], 0) + 1
# Dict of rules
rules = {}
for i in range(2, len(input)):
    p1, p2 = input[i].split(' -> ')
    rules[p1] = p2


def step(pairs, rules):
    new_pairs = {}
    for pair in pairs:
        if pair in rules:
            insert = rules[pair]
            new_pairs[''.join([pair[0], insert])] = new_pairs.get(''.join([pair[0], insert]), 0) + pairs[pair]
            new_pairs[''.join([insert, pair[1]])] = new_pairs.get(''.join([insert, pair[1]]), 0) + pairs[pair]
        else:
            new_pairs[pair] = new_pairs.get(pair, 0) + pairs[pair]

    return new_pairs


def score(pairs, template):
    """
        Each letter in the final string appears in two pairs, except for the first and last one
    """
    scores = {}
    for pair in pairs:
        scores[pair[0]] = scores.get(pair[0], 0) + pairs[pair]
        scores[pair[1]] = scores.get(pair[1], 0) + pairs[pair]
    for letter in scores:
        scores[letter] = scores[letter]//2

    scores[template[0]] += 1
    scores[template[-1]] += 1

    scores = [scores[l] for l in scores]
    return max(scores) - min(scores)


def run(pairs, rules, template):
    for i in range(10):
        pairs = step(pairs, rules)

    p1_sol = score(pairs, template)

    for i in range(30):
        pairs = step(pairs, rules)

    p2_sol = score(pairs, template)

    return p1_sol, p2_sol


p1_sol, p2_sol = run(pairs, rules, template)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
