from aoc import AOC
from collections import defaultdict

aoc = AOC(23,  2017, __file__)

input = aoc.input.strip().split('\n')

def parseInt(mem, token):
    try:
        return int(token)
    except:
        return mem[token]

def step(mem, pc):
    tokens = input[pc].split()
    isMul = False

    if tokens[0] == 'set':
        mem[tokens[1]] = parseInt(mem, tokens[2])
    elif tokens[0] == 'sub':
        mem[tokens[1]] -= parseInt(mem, tokens[2])
    elif tokens[0] == 'mul':
        mem[tokens[1]] *= parseInt(mem,  tokens[2])
        isMul = True
    elif tokens[0] == 'jnz':
        if parseInt(mem, tokens[1]) != 0:
            return pc + parseInt(mem, tokens[2]), False
    
    return pc + 1, isMul

def part1():
    mem = defaultdict(int)
    pc = muls = 0
    while 0 <= pc < len(input):
        pc, isMul = step(mem, pc)
        muls += isMul

    return muls

def part2():
    # Nombre de non-premiers entre 109 900 et 126 900 inclus
    s = [True] * 126_901
    s[0] = False
    s[1] = False
    for i in range(126_901):
        if s[i]:
            j = 2
            while i * j < 126_901:
                s[i * j] = False
                j += 1
    
    r = 0
    for i in range(109_900, 126_901, 17):
        if not s[i]:
            r += 1
    
    return r

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
