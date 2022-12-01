from aoc import AOC
from collections import defaultdict

aoc = AOC(18,  2017, __file__)

input = aoc.input.strip().split('\n')

def parseInt(mem, token):
    try:
        return int(token)
    except:
        return mem[token]

def step(mem, pc, recv, other_recv):
    tokens = input[pc].split()

    if tokens[0] == 'snd':
        other_recv.append(parseInt(mem, tokens[1]))
    elif tokens[0] == 'set':
        mem[tokens[1]] = parseInt(mem, tokens[2])
    elif tokens[0] == 'add':
        mem[tokens[1]] += parseInt(mem, tokens[2])
    elif tokens[0] == 'mul':
        mem[tokens[1]] *= parseInt(mem,  tokens[2])
    elif tokens[0] == 'mod':
        mem[tokens[1]] %= parseInt(mem, tokens[2])
    elif tokens[0] == 'rcv':
        if len(recv) == 0:
            return pc
        mem[tokens[1]] = recv[0]
        recv.pop(0)
    elif tokens[0] == 'jgz':
        if parseInt(mem, tokens[1]) > 0:
            return pc + parseInt(mem, tokens[2])
    
    return pc + 1

def part1():
    mem = defaultdict(int)
    send = []
    pc = 0
    while 0 <= pc < len(input):
        if input[pc].split()[0] == 'rcv' and parseInt(mem, input[pc].split()[1]) != 0:
            return send[-1]
        pc = step(mem, pc, [], send)

def part2():
    mems = [defaultdict(int) for id in range(2)]
    for id in range(2): mems[id]['p'] = id

    recvs = [[] for id in range(2)]
    pcs = [0 for id in range(2)]
    nb_1_sent = 0

    # Run programs
    while any([0 <= pc < len(input) for pc in pcs]):
        old_pcs = pcs[:]
        for id in range(2):
            if 0 <= pcs[id] < len(input):
                if id == 1 and input[pcs[id]].split()[0] == 'snd':
                    nb_1_sent += 1
                pcs[id] = step(mems[id], pcs[id], recvs[id], recvs[1 - id])

        if old_pcs == pcs:
            break

    return nb_1_sent

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
