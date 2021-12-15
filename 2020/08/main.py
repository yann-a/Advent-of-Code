from aoc import AOC

aoc = AOC(8,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')


def read_program(seen, pc, acc, changed_inst):
    sols, had_seen_pc = {}, False

    try:
        if seen[pc]:
            had_seen_pc = True
            if changed_inst:
                return {}
            else:
                sols[1] = acc

        seen[pc] = True
        inst, v = input[pc].split()

        if inst == 'nop':
            if not changed_inst:
                res = read_program(seen[:], pc + int(v), acc, True)
                if 2 in res: sols[2] = res[2]

            if not had_seen_pc:
                res = read_program(seen[:], pc + 1, acc, changed_inst)
                if 1 in res: sols[1] = res[1]
                if 2 in res: sols[2] = res[2]

        elif inst == 'jmp':
            if not changed_inst:
                res = read_program(seen[:], pc + 1, acc, True)
                if 2 in res: sols[2] = res[2]

            if not had_seen_pc:
                res = read_program(seen[:], pc + int(v), acc, changed_inst)
                if 1 in res: sols[1] = res[1]
                if 2 in res: sols[2] = res[2]

        elif inst == 'acc':
            if not had_seen_pc:
                res = read_program(seen[:], pc + 1, acc + int(v), changed_inst)
                if 1 in res: sols[1] = res[1]
                if 2 in res: sols[2] = res[2]
    except:
        return {2: acc}

    return sols


sols = read_program([False] * len(input), 0, 0, False)
p1_sol, p2_sol = sols[1], sols[2]

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
