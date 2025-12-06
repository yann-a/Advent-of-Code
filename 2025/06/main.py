from aoc import AOC

aoc = AOC(6,  2025, __file__)

input = aoc.input.rstrip().split('\n')
#input = aoc.get_example(0).rstrip().split('\n')

def part1():
    numbers, operators = input[:-1], input[-1]
    numbers = [list(map(int, line.split())) for line in numbers]
    operators = operators.split()

    s = 0
    for j in range(len(numbers[0])):
        op = operators[j]

        t = 1 if op == '*' else 0
        for i in range(len(numbers)):
            if op == '*':
                t *= numbers[i][j]
            else:
                t += numbers[i][j]
        
        s += t

    return s

def part2():
    _numbers, operators = input[:-1], input[-1]
    space_indexes = [-1] + [j for j in range(len(_numbers[0])) if all(_numbers[i][j] == ' ' for i in range(len(_numbers)))] + [len(_numbers[0])]
    numbers = []
    for _line in _numbers:
        line = []
        for k1, k2 in zip(space_indexes, space_indexes[1:]):
            line.append(_line[k1 + 1:k2])
        numbers.append(line)
    operators = operators.split()

    s = 0
    for j in range(len(numbers[0])):
        op = operators[j]

        t = 1 if op == '*' else 0
        for k in range(len(numbers[0][j]) - 1, -1, -1):
            n = 0
            for i in range(len(numbers)):
                if numbers[i][j][k] != ' ':
                    n = n * 10 + int(numbers[i][j][k])

            if op == '*':
                t *= n
            else:
                t += n
        
        s += t

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
