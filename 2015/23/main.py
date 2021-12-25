from aoc import AOC

aoc = AOC(23,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def get_b(a=0, b=0):
    memory = {'a': a, 'b': b}
    pc = 0

    while pc < len(input):
        tokens = input[pc].split()

        if tokens[0] == 'hlf':
            memory[tokens[1]] //= 2
            pc += 1
        elif tokens[0] == 'tpl':
            memory[tokens[1]] *= 3
            pc += 1
        elif tokens[0] == 'inc':
            memory[tokens[1]] += 1
            pc += 1
        elif tokens[0] == 'jmp':
            pc += int(tokens[1])
        elif tokens[0] == 'jie':
            if memory[tokens[1][:-1]] % 2 == 0:
                pc += int(tokens[2])
            else:
                pc += 1
        elif tokens[0] == 'jio':
            if memory[tokens[1][:-1]] == 1:
                pc += int(tokens[2])
            else:
                pc += 1

    return memory['b']

p1_sol = get_b()
p2_sol = get_b(a=1)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
