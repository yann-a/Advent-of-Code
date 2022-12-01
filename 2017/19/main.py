from aoc import AOC

aoc = AOC(19,  2017, __file__)

input = aoc.input.split('\n')[:-1]

x, y, d, steps, last_letter_steps = input[0].index('|'), 0, 'S', 0, 0
letters = ''
while True:
    x, y = x + (d == 'E') - (d == 'W'), y + (d == 'S') - (d == 'N')
    steps += 1

    if x < 0 or len(input[0]) <= x or y < 0 or len(input) <= y:
        break

    if input[y][x] not in ['|', '-', '+', ' ']:
        letters += input[y][x]
        last_letter_steps = steps + 1
    if input[y][x] == '+':
        if d != 'S' and y > 0 and input[y-1][x] not in ['-', '+', ' ']:
            d = 'N'
        elif d != 'E' and x > 0 and input[y][x-1]  not in ['|', '+', ' ']:
            d = 'W'
        elif d != 'N' and y < len(input) - 1 and input[y+1][x] not in ['-', '+', ' ']:
            d = 'S'
        else:
            d = 'E'

p1_sol = letters
p2_sol = last_letter_steps

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
