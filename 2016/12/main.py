from aoc import AOC

aoc = AOC(12,  2016, __file__)

input = aoc.input.strip().split('\n')

def parseInt(string):
    try:
        return int(string)
    except:
        return None

def get_a(mem):
    mem = mem.copy()
    pc = 0
    while pc < len(input):
        tokens = input[pc].split()

        if tokens[0] == 'cpy':
            if parseInt(tokens[1]) is not None:
                mem[tokens[2]] = parseInt(tokens[1])
            else:
                mem[tokens[2]] = mem[tokens[1]]
            pc += 1
        elif tokens[0] == 'inc':
            mem[tokens[1]] += 1
            pc += 1
        elif tokens[0] == 'dec':
            mem[tokens[1]] -= 1
            pc += 1
        else:
            if (parseInt(tokens[1]) is not None and parseInt(tokens[1]) != 0) or (tokens[1] in 'abcd' and mem[tokens[1]] != 0):
                pc += parseInt(tokens[2])
            else:
                pc += 1
    return mem['a']

mem = {r: 0 for r in 'abcd'}
p1_sol = get_a(mem)
mem['c'] = 1
p2_sol = get_a(mem)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
