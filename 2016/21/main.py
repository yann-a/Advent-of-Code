from aoc import AOC

aoc = AOC(21,  2016, __file__)

input = aoc.input.strip().split('\n')

def reverse_instruction(instruction):
    instruction = instruction.split()

    if instruction[0] == 'rotate' and instruction[1] in ['left', 'right']:
        instruction[1] = 'left' if instruction[1] == 'right' else 'right'
    elif instruction[0] == 'rotate':
        instruction[0] = 'unrotate'
    elif instruction[0] == 'move':
        instruction[2], instruction[5] = instruction[5], instruction[2]

    return ' '.join(instruction)

def execute_instructions(string, instructions):
    string = list(string)
    for instruction in instructions:
        instruction = instruction.split()

        if instruction[0] == 'swap' and instruction[1] == 'position':
            p1, p2 = int(instruction[2]), int(instruction[5])
            string[p1], string[p2] = string[p2], string[p1]
        elif instruction[0] == 'swap' and instruction[1] == 'letter':
            l1, l2 = instruction[2], instruction[5]
            string = [l1 if el == l2 else l2 if el == l1 else el for el in string]
        elif instruction[0] == 'rotate':
            if instruction[1] == 'right':
                steps = int(instruction[2])
                string = string[-steps:] + string[:-steps]
            elif instruction[1] == 'left':
                steps = int(instruction[2])
                string = string[steps:] + string[:steps]
            else:
                steps = string.index(instruction[6])
                if steps >= 4:
                    steps += 2
                else:
                    steps += 1
                steps %= len(string)
                string = string[-steps:] + string[:-steps]
        elif instruction[0] == 'reverse':
            p1, p2 = int(instruction[2]), int(instruction[4])
            string = string[:p1] + string[p1:p2 + 1][::-1] + string[p2 + 1:]
        elif instruction[0] == 'move':
            x, y = int(instruction[2]), int(instruction[5])

            l = string[x]
            string = string[:x] + string[x + 1:]
            string = string[:y] + [l] + string[y:]
        elif instruction[0] == 'unrotate':
            for rotate_nb in range(len(string)):
                string_attempt = string[rotate_nb:] + string[:rotate_nb]

                steps = string_attempt.index(instruction[6])
                if steps >= 4:
                    steps += 2
                else:
                    steps += 1
                steps %= len(string)
                string_attemptrot = string_attempt[-steps:] + string_attempt[:-steps]

                if string_attemptrot == string:
                    string = string_attempt
                    break


    return ''.join(string)

p1_sol = execute_instructions('abcdefgh', input)
p2_sol = execute_instructions('fbgdceah', list(map(reverse_instruction, input[::-1])))

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
