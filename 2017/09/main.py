from aoc import AOC

aoc = AOC(9,  2017, __file__)

#input = aoc.get_example(0).strip()
input = aoc.input.strip()

stream = (c for c in input)

def readGarbage(stream):
    nb_chars = 0
    c = ''
    while c != '>':
        c = next(stream)

        while c == '!':
            c = next(stream)
            c = next(stream)

        if c != '>':
            nb_chars += 1

    return nb_chars

def readGroup(stream, depth):
    score = nb_garbage = 0
    c = ''
    while c != '}':
        c = next(stream)
        if c == '<':
            nb_garbage += readGarbage(stream)
        elif c == '{':
            rec_score, rec_garbage = readGroup(stream, depth + 1)
            score += depth + rec_score
            nb_garbage += rec_garbage

    return score, nb_garbage

def countGroups(stream):
    c = next(stream)
    score, nb_garbage = readGroup(stream, 2)
    return 1 + score, nb_garbage

p1_sol, p2_sol = countGroups(stream)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)