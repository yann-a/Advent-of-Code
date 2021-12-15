from aoc import AOC

aoc = AOC(4,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

p1_sol = 0
p2_sol = 0

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
curr_pass_exists = [False] * len(FIELDS)
curr_pass_valid = [False] * len(FIELDS)
i = 0
while i < len(input):
    if input[i] == '':
        if all(curr_pass_exists):
            p1_sol += 1
        if all(curr_pass_valid):
            p2_sol += 1
        curr_pass_exists = [False] * len(FIELDS)
        curr_pass_valid = [False] * len(FIELDS)
    else:
        fields = input[i].split()
        for val in fields:
            name, v = val.split(':')
            if name in FIELDS:
                curr_pass_exists[FIELDS.index(name)] = True

            if name == 'byr' and 1920 <= int(v) <= 2002:
                curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'iyr' and 2010 <= int(v) <= 2020:
                curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'eyr' and 2020 <= int(v) <= 2030:
                curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'hgt':
                if v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193:
                    curr_pass_valid[FIELDS.index(name)] = True
                elif v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76:
                    curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'hcl':
                if v[0] == '#' and len(v) == 7 and all([c in '0123456789abcdef' for c in v[1:]]):
                    curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'ecl' and v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                curr_pass_valid[FIELDS.index(name)] = True
            elif name == 'pid' and len(v) == 9 and all([c in '0123456789' for c in v]):
                curr_pass_valid[FIELDS.index(name)] = True
    i += 1
if all(curr_pass_exists):
    p1_sol += 1
if all(curr_pass_valid):
    p2_sol += 1

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
