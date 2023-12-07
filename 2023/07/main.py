from aoc import AOC

aoc = AOC(7,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

cards = 'AKQJT98765432'
cards2 = 'AKQT98765432J'

def getHandType(hand):
    for c in cards:
        if hand.count(c) == 5:
            return 0
    for c in cards:
        if hand.count(c) == 4:
            return 1
    for c in cards:
        for c2 in cards:
            if c2 != c and hand.count(c) == 3 and hand.count(c2) == 2:
                return 2
    for c in cards:
        if hand.count(c) == 3:
            return 3
    for c in cards:
        for c2 in cards:
            if c2 != c and hand.count(c) == 2 and hand.count(c2) == 2:
                return 4
    for c in cards:
        if hand.count(c) == 2:
            return 5

    return 6

def getHandType2(hand, js):
    if hand.count('J') == len(js):
        for i in range(len(js)):
            j = hand.index('J')
            hand = hand[:j] + js[i] + hand[j + 1:]

        for c in cards2:
            if hand.count(c) == 5:
                return 0
        for c in cards2:
            if hand.count(c) == 4:
                return 1
        for c in cards2:
            for c2 in cards2:
                if c2 != c and hand.count(c) == 3 and hand.count(c2) == 2:
                    return 2
        for c in cards2:
            if hand.count(c) == 3:
                return 3
        for c in cards2:
            for c2 in cards2:
                if c2 != c and hand.count(c) == 2 and hand.count(c2) == 2:
                    return 4
        for c in cards2:
            if hand.count(c) == 2:
                return 5

        return 6
    else:
        m = 6
        for v in cards2[:-1]:
            m = min(m, getHandType2(hand, js + [v]))

        return m

def part1():
    decks = []
    for line in input:
        c, bid = line.split()
        decks.append((c, int(bid)))

    decks.sort(key=lambda t: [getHandType(t[0])] + list(map(lambda c: cards.index(c), t[0])), reverse=True)

    return sum((i + 1) * decks[i][1] for i in range(len(decks)))

def part2():
    decks = []
    for line in input:
        c, bid = line.split()
        decks.append((c, int(bid)))

    decks.sort(key=lambda t: [getHandType2(t[0], [])] + list(map(lambda c: cards2.index(c), t[0])), reverse=True)

    return sum((i + 1) * decks[i][1] for i in range(len(decks)))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)