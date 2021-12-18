from aoc import AOC

aoc = AOC(22,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

decks = (list(map(int, input[0].split('\n')[1:])), list(map(int, input[1].split('\n')[1:])))

def step1(decks):
    """
        input: a tuple with two decks
        output:
            - int winner: -1 if no winner; 0 or 1 if there is a winner
            - the two new decks
    """
    if decks[0][0] > decks[1][0]:
        decks = decks[0][1:] + [decks[0][0], decks[1][0]], decks[1][1:]

        if len(decks[1]) == 0: return 0, decks
        else: return -1, decks
    else:
        decks = decks[0][1:], decks[1][1:] + [decks[1][0], decks[0][0]]

        if len(decks[0]) == 0: return 1, decks
        else: return -1, decks

def step2(decks):
    if len(decks[0][1:]) >= decks[0][0] and len(decks[1][1:]) >= decks[1][0]:
        win, _ = game2((decks[0][1:decks[0][0] + 1], decks[1][1:decks[1][0] + 1]))

        if win == 0:
            decks = decks[0][1:] + [decks[0][0], decks[1][0]], decks[1][1:]

            if len(decks[1]) == 0: return 0, decks
            else: return -1, decks
        else:
            decks = decks[0][1:], decks[1][1:] + [decks[1][0], decks[0][0]]

            if len(decks[0]) == 0: return 1, decks
            else: return -1, decks
    else:
        if decks[0][0] > decks[1][0]:
            decks = decks[0][1:] + [decks[0][0], decks[1][0]], decks[1][1:]

            if len(decks[1]) == 0: return 0, decks
            else: return -1, decks
        else:
            decks = decks[0][1:], decks[1][1:] + [decks[1][0], decks[0][0]]

            if len(decks[0]) == 0: return 1, decks
            else: return -1, decks

def score(deck):
    return sum([(i + 1) * e for i, e in enumerate(deck[::-1])])

def game1(decks):
    win = -1
    while win == -1:
        win, decks = step1(decks)

    return score(decks[win])

def game2(decks):
    deck1_history = [decks[0][:]]
    deck2_history = [decks[1][:]]

    win = -1
    while win == -1:
        win, decks = step2(decks)

        if win == -1:
            if decks[0] in deck1_history or decks[1] in deck2_history:
                win = 0

            deck1_history.append(decks[0][:])
            deck2_history.append(decks[1][:])

    return win, score(decks[win])

p1_sol = game1(decks)
_, p2_sol = game2(decks)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
