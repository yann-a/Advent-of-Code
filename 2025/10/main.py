from aoc import AOC
from queue import PriorityQueue
import z3

aoc = AOC(10,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0
    for line in input:
        line = line.split()
        lights, buttons, joltage = line[0], line[1:-1], line[-1]
        lights = lights[1:-1]
        buttons = [list(map(int, button[1:-1].split(','))) for button in buttons]
        joltage = list(map(int, joltage[1:-1].split(',')))

        q = PriorityQueue()
        q.put((0, '.' * len(lights)))
        seen = set()

        while not q.empty():
            n, l = q.get()

            if l in seen:
                continue
            seen.add(l)

            if l == lights:
                s += n
                break

            for button in buttons:
                nl = list(l)
                for i in button:
                    nl[i] = '.' if nl[i] == '#' else '#'
                nl = ''.join(nl)

                if nl not in seen:
                    q.put((n + 1, nl))

    return s

def part2():
    _s = 0
    for line in input:
        line = line.split()
        lights, buttons, joltage = line[0], line[1:-1], line[-1]
        lights = lights[1:-1]
        buttons = [list(map(int, button[1:-1].split(','))) for button in buttons]
        joltage = list(map(int, joltage[1:-1].split(',')))

        s = z3.Optimize()
        presses = [z3.Int(f'button{i}') for i in range(len(buttons))]
        for i in range(len(buttons)):
            s.add(presses[i] >= 0)
        for i in range(len(joltage)):
            s.add(sum([presses[j] for j in range(len(buttons)) if i in buttons[j]]) == joltage[i])
        s.minimize(sum(presses))

        assert s.check() == z3.sat

        r = s.model()
        _s += sum(r[presses[i]].as_long() for i in range(len(buttons)))

    return _s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
