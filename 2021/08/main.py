from aoc import AOC

aoc = AOC(8,  2021, __file__)

#input = aoc.example
input = aoc.input

indexes = 'abcdefg'

nb_unique = 0
somme = 0
for line in input.strip().split('\n'):
    in_, out = line.strip().split('|')
    in_ = in_.split()
    out = out.split()

    # signal -> possible segments it controls
    poss = {l: set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) for l in indexes}

    # Compte part 1's answer
    for output in out:
        if len(output) in [2, 3, 4, 7]:
            nb_unique += 1

    # eliminate possiblities based on the input values
    for _in in in_:
        if len(_in) == 2:  # 1
            for el in _in:
                poss[el] = poss[el].intersection(set(['c', 'f']))
            for el in indexes:
                if el not in _in:
                    poss[el] = poss[el] - set(['c', 'f'])
        elif len(_in) == 3:  # 7
            for el in _in:
                poss[el] = poss[el].intersection(set(['a', 'c', 'f']))
            for el in indexes:
                if el not in _in:
                    poss[el] = poss[el] - set(['a', 'c', 'f'])
        elif len(_in) == 4:  # 4
            for el in _in:
                poss[el] = poss[el].intersection(set(['b', 'c', 'd', 'f']))
            for el in indexes:
                if el not in _in:
                    poss[el] = poss[el] - set(['b', 'c', 'd', 'f'])

        elif len(_in) == 5:  # 2, 3, 5
            for el in indexes:
                if el not in _in:
                    poss[el] = poss[el] - set(['a', 'd', 'g'])
        elif len(_in) == 6:  # 6, 9, 0
            for el in indexes:
                if el not in _in:
                    poss[el] = poss[el] - set(['a', 'b', 'f', 'g'])

    # determines the actual mapping by removing the last ambiguities
    mapping = {}
    while len(mapping) < 7:
        for el in indexes:
            if el not in mapping:
                if len(poss[el]) == 1:
                    for v in poss[el]:
                        mapping[el] = v
                else:
                    for v in poss[el]:
                        if v in mapping.values():
                            poss[el].remove(v)
                            break

    # compute the sum
    for k, _out in enumerate(out):
        lit_segments = [mapping[el] for el in _out]

        if len(lit_segments) == 6 and 'd' not in lit_segments:  # 0
            pass
        elif len(lit_segments) == 2:  # 1
            somme += 10**(3-k)
        elif len(lit_segments) == 5 and 'e' in lit_segments:  # 2
            somme += 2*10**(3-k)
        elif len(lit_segments) == 5 and 'b' not in lit_segments:  # 3
            somme += 3*10**(3-k)
        elif len(lit_segments) == 4:  # 4
            somme += 4*10**(3-k)
        elif len(lit_segments) == 5:  # 5
            somme += 5*10**(3-k)
        elif len(lit_segments) == 6 and 'c' not in lit_segments:  # 6
            somme += 6*10**(3-k)
        elif len(lit_segments) == 3:  # 7
            somme += 7*10**(3-k)
        elif len(lit_segments) == 7:  # 8
            somme += 8*10**(3-k)
        else:  # 9
            somme += 9*10**(3-k)

print('Part 1:', nb_unique)
#aoc.submit(1, str(nb_unique))
print('Part 2:', somme)
#aoc.submit(2, str(somme))
