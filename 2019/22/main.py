from aoc import AOC
from math import ceil

aoc = AOC(22,  2019, __file__)

input = aoc.input.strip().split('\n')

def part1(N, el):
    cards = list(range(N))

    for instruction in input:
        tokens = instruction.split()

        if instruction == 'deal into new stack':
            cards.reverse()
        elif tokens[0] == 'cut':
            cut_n = int(tokens[1])

            cards = cards[cut_n:] + cards[:cut_n]
        elif tokens[0] == 'deal':
            deal_n = int(tokens[3])

            oldcards = cards[:]

            pt = 0
            for i in range(N):
                cards[pt] = oldcards[i]
                pt = (pt + deal_n) % N

    return cards.index(el)

def part2(N, R, final_pos):
    # apply operations in reverse order twice to get values for the two last rounds
    # notice the operations are all linear
    pos = final_pos
    int_pos = [pos]

    for _ in range(2):
        for instruction in input[::-1]:
            tokens = instruction.split()

            if instruction == 'deal into new stack':
                pos = N - 1 - pos
            elif tokens[0] == 'cut':
                cut_n = int(tokens[1])

                pos = (pos + cut_n) % N
            elif tokens[0] == 'deal':
                deal_n = int(tokens[3])
        
                pos = (pow(deal_n, -1, N) * pos) % N
            
        int_pos.append(pos)

    # find A, B such that
    #     int_pos[1] = A * int_pos[0] + B
    #     int_pos[2] = A * int_pos[1] + B
    A = (int_pos[1] - int_pos[2]) * pow(int_pos[0] - int_pos[1], -1, N) % N
    B = (int_pos[1] - A * int_pos[0]) % N

    # f^(n)(X) = A^n * X + (A^n - 1) / (A - 1) * B
    # Apply it the required number of times
    return (pow(A, R, N) * final_pos + (pow(A, R, N) - 1) * pow(A - 1, -1, N) * B) % N

p1_sol = part1(10_007, 2019)
p2_sol = part2(119_315_717_514_047, 101_741_582_076_661, 2020)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
