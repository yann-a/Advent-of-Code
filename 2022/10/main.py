from aoc import AOC

aoc = AOC(10,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    X = 1
    cycle_num = 1
    s = 0
    for inst in input:
        if inst == 'noop':
            cycle_num += 1
            if (cycle_num - 20) % 40 == 0:
                s += cycle_num * X
        else:
            if (cycle_num + 1 - 20) % 40 == 0:
                s += (cycle_num + 1) * X

            cycle_num += 2
            X += int(inst.split()[1])

            if (cycle_num - 20) % 40 == 0:
                s += cycle_num * X

    return s

def part2():
    X = 1
    cycle_num = 1
    image = ['' for _ in range(6)]
    image[0] = '#'
    for inst in input:
        try:
            if inst == 'noop':
                cycle_num += 1
                
                i = (cycle_num - 1) // 40
                j = (cycle_num - 1) % 40
                if abs(j - X) <= 1:
                    image[i] += '#'
                else:
                    image[i] += '.'
            else:
                i = cycle_num // 40
                j = cycle_num % 40
                if abs(j - X) <= 1:
                    image[i] += '#'
                else:
                    image[i] += '.'

                cycle_num += 2
                X += int(inst.split()[1])

                i = (cycle_num - 1) // 40
                j = (cycle_num - 1) % 40
                if abs(j - X) <= 1:
                    image[i] += '#'
                else:
                    image[i] += '.'
        except:
            pass

    for row in image:
        print(row)

p1_sol = part1()
part2()
p2_sol = 'ERCREPCJ'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
