from aoc import AOC

aoc = AOC(15,  2020, __file__)

#input = list(map(int, "0,3,6".split(',')))
input = list(map(int, "15,5,1,4,7,0".split(',')))

last_spoken, prev = {}, None
for turn in range(30_000_000):
    if turn == 2020:
        p1_sol = prev

    if turn < len(input):
        if prev is not None:
            last_spoken[prev] = turn - 1
        prev = input[turn]
    else:
        if prev in last_spoken:
            delay = (turn - 1) - last_spoken[prev]
            last_spoken[prev] = turn - 1
            prev = delay
        else:
            last_spoken[prev] = turn - 1
            prev = 0

p2_sol = prev

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
