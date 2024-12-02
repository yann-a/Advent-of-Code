from aoc import AOC

aoc = AOC(2,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0

    for line in input:
        levels = list(map(int, line.split()))

        safe = True
        incr = True
        decr = True

        for i in range(len(levels) - 1):
            if abs(levels[i] - levels[i + 1]) == 0 or abs(levels[i] - levels[i + 1]) > 3:
                safe = False

            if levels[i] >= levels[i + 1]:
                incr = False

            if levels[i + 1] >= levels[i]:
                decr = False

        if safe and (incr or decr):
            s += 1

    return s

def part2():
    s = 0

    for line in input:
        _levels = list(map(int, line.split()))

        for i in range(len(_levels)):
            levels = _levels[:]
            levels.pop(i)

            safe = True
            incr = True
            decr = True

            for i in range(len(levels) - 1):
                if abs(levels[i] - levels[i + 1]) == 0 or abs(levels[i] - levels[i + 1]) > 3:
                    safe = False

                if levels[i] >= levels[i + 1]:
                    incr = False

                if levels[i + 1] >= levels[i]:
                    decr = False

            if safe and (incr or decr):
                s += 1
                break

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
