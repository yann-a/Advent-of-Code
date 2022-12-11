from aoc import AOC

aoc = AOC(11,  2022, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    monkeys = []

    for monkey in input:
        monkey = monkey.split('\n')
        items = list(map(int, ''.join(monkey[1].split()[2:]).split(',')))
        operation = monkey[2].split()[4], monkey[2].split()[5]
        div_test = int(monkey[3].split()[3])
        if_true = int(monkey[4].split()[5])
        if_false = int(monkey[5].split()[5])

        monkeys.append([items, operation, div_test, if_true, if_false])
        
    activity = [0 for _ in monkeys]
    for round in range(20):
        for i, monkey in enumerate(monkeys):
            items, operation, div_test, if_true, if_false = monkey
            for worry in items:
                activity[i] += 1

                if operation[0] == '+': worry += int(operation[1])
                else: worry *= (worry if operation[1] == 'old' else int(operation[1]))

                worry //= 3

                if worry % div_test == 0: monkeys[if_true][0].append(worry)
                else: monkeys[if_false][0].append(worry)

                monkeys[i][0] = []

    activity.sort()
    return activity[-2] * activity[-1]

def part2():
    monkeys = []

    for monkey in input:
        monkey = monkey.split('\n')
        items = list(map(int, ''.join(monkey[1].split()[2:]).split(',')))
        operation = monkey[2].split()[4], monkey[2].split()[5]
        div_test = int(monkey[3].split()[3])
        if_true = int(monkey[4].split()[5])
        if_false = int(monkey[5].split()[5])

        monkeys.append([items, operation, div_test, if_true, if_false])
        
    activity = [0 for _ in monkeys]
    for round in range(10_000):
        for i, monkey in enumerate(monkeys):
            items, operation, div_test, if_true, if_false = monkey
            for worry in items:
                activity[i] += 1

                if operation[0] == '+': worry += int(operation[1])
                else: worry *= (worry if operation[1] == 'old' else int(operation[1]))

                worry %= 9699690 # 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19, pgcd of the values we test as divisors

                if worry % div_test == 0: monkeys[if_true][0].append(worry)
                else: monkeys[if_false][0].append(worry)

                monkeys[i][0] = []

    activity.sort()
    return activity[-2] * activity[-1]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
