from aoc import AOC

aoc = AOC(23,  2016, __file__)

input = aoc.input.strip().split('\n')

def parseInt(string):
    try:
        return int(string)
    except:
        return None

def get_a(mem, code):
    mem = mem.copy()
    code = code[:]
    pc = 0
    while pc < len(code):
        tokens = code[pc].split()

        if tokens[0] == 'cpy':
            if parseInt(tokens[1]) is not None:
                mem[tokens[2]] = parseInt(tokens[1])
            else:
                mem[tokens[2]] = mem[tokens[1]]
            pc += 1
        elif tokens[0] == 'inc':
            if parseInt(tokens[1]) is None:
                mem[tokens[1]] += 1
            pc += 1
        elif tokens[0] == 'dec':
            if parseInt(tokens[1]) is None:
                mem[tokens[1]] -= 1
            pc += 1
        elif tokens[0] == 'tgl':
            if parseInt(tokens[1]) is not None:
                toggled_instruction = pc + parseInt(tokens[1])
            else:
                toggled_instruction = pc + mem[tokens[1]]

            if 0 <= toggled_instruction < len(code):
                inst_tokens = code[toggled_instruction].split()

                if len(inst_tokens) == 2:
                    if inst_tokens[0] == 'inc':
                        code[toggled_instruction] = ' '.join(['dec'] + inst_tokens[1:])
                    else:
                        code[toggled_instruction] = ' '.join(['inc'] + inst_tokens[1:])
                elif len(inst_tokens) == 3:
                    if inst_tokens[0] == 'jnz':
                        code[toggled_instruction] = ' '.join(['cpy'] + inst_tokens[1:])
                    else:
                        code[toggled_instruction] = ' '.join(['jnz'] + inst_tokens[1:])
            pc += 1
        elif tokens[0] == 'mlt':
            if parseInt(tokens[1]) is not None and parseInt(tokens[2]) is not None:
                mem[tokens[3]] = parseInt(tokens[1]) * parseInt(tokens[2])
            elif parseInt(tokens[1]) is not None:
                mem[tokens[3]] = parseInt(tokens[1]) * mem[tokens[2]]
            elif parseInt(tokens[2]) is not None:
                mem[tokens[3]] = mem[tokens[1]] * parseInt(tokens[2])
            else:
                mem[tokens[3]] = mem[tokens[1]] * mem[tokens[2]]
            pc += 1
        else:
            if (parseInt(tokens[1]) is not None and parseInt(tokens[1]) != 0) or (tokens[1] in 'abcd' and mem[tokens[1]] != 0):
                if parseInt(tokens[2]) is not None:
                    pc += parseInt(tokens[2])
                else:
                    pc += mem[tokens[2]]
            else:
                pc += 1
    return mem['a']

mem = {r: 0 for r in 'abcd'}
mem['a'] = 7
p1_sol = get_a(mem, input)

mem['a'] = 12
input[3] = 'mlt a b a'
input[4] = 'cpy 0 c'
input[5] = 'cpy 0 d'
input[6] = 'cpy a a'
input[7] = 'cpy a a'
input[8] = 'cpy a a'
input[9] = 'cpy a a'

input[11] = 'mlt 2 b c'
input[12] = 'cpy 0 d'
input[13] = 'cpy a a'
input[14] = 'cpy a a'
input[15] = 'cpy a a'
p2_sol = get_a(mem, input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
