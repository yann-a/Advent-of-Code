from aoc import AOC

aoc = AOC(12,  2025, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    shapes, regions = input[:-1], input[-1]
    shapes = [shape.split('\n')[1:] for shape in shapes]
    regions = regions.split('\n')

    s = 0
    for region in regions:
        shape, shapecount = region.split(': ')
        w, h = map(int, shape.split('x'))
        shapecount = list(map(int, shapecount.split()))

        if w * h >= sum(sc * len(shape) * len(shape[0]) for sc, shape in zip(shapecount, shapes)):
            s += 1

    return s

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
