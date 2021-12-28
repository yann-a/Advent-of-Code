from aoc import AOC

aoc = AOC(8,  2016, __file__)

input = aoc.input.strip().split('\n')

screen = [[' ' for _ in range(50)] for _ in range(6)]
for instruction in input:
    instruction = instruction.split()
    
    if instruction[0] == 'rect':
        a, b = instruction[1].split('x')
        for y in range(int(b)):
            for x in range(int(a)):
                screen[y][x] = '#'
    else:
        a = int(instruction[2].split('=')[1])
        b = int(instruction[-1])

        if instruction[1] == 'row':
            screen[a] = screen[a][50 - b:] + screen[a][:50 - b]
        else:
            old_col = [screen[x][a] for x in range(6)]
            for x in range(6):
                screen[x][a] = old_col[(x - b) % 6]

nb_lit = sum([sum([el == '#' for el in col]) for col in screen])
for row in screen:
    print(''.join(row))

p1_sol = nb_lit
# p2 solution readable in stdout
p2_sol = 'EFEYKFRFIJ'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
