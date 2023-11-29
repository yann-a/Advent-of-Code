from aoc import AOC
from intcode import *

aoc = AOC(13,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)
    game_map = defaultdict(int)

    intcode.run()
    while len(intcode.output) > 0:
        x, y, tile_id = [intcode.getOutput() for _ in range(3)]
        game_map[(x, y)] = tile_id

    return sum(game_map[p] == 2 for p in game_map)

symbols = ' #X-o'

def part2():
    program = list(map(int, input[0].split(',')))
    program[0] = 2
    intcode = IntCodeProgram(program)
    game_map = defaultdict(int)
    scores = []

    while not intcode.run():
        while len(intcode.output) > 0:
            x, y, tile_id = [intcode.getOutput() for _ in range(3)]
            if x == -1 and y == 0: scores.append(tile_id)
            else: game_map[(x, y)] = tile_id

        """
        print(scores)
        for line in range(30):
            for x in range(50):
                print(symbols[game_map[(x, line)]], end='')
            print()
        """

        bx = [x for (x, y) in game_map if game_map[(x, y)] == 4][0]
        px = [x for (x, y) in game_map if game_map[(x, y)] == 3][0]

        if bx < px: intcode.addInput(-1)
        elif bx > px: intcode.addInput(1)
        else: intcode.addInput(0)

    while len(intcode.output) > 0:
        x, y, tile_id = [intcode.getOutput() for _ in range(3)]
        if x == -1 and y == 0: scores.append(tile_id)
        else: game_map[(x, y)] = tile_id

    return scores[-1]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
