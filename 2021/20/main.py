from aoc import AOC

aoc = AOC(20,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

algorithm = ''.join(map(lambda l: l.strip(), input[0]))

image = input[1].split('\n')
outside = '0'

def neighbours(image, x, y, outside):
    nb_str = ''
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if 0 <= y + dy < len(image) and 0 <= x + dx < len(image[0]):
                nb_str += '1' if image[y + dy][x + dx] == '#' else '0'
            else:
                nb_str += outside

    return int(nb_str, base=2)

def apply(image, algorithm, outside):
    new_image = [[None for _ in range(-1, len(image[0]) + 1)] for _ in range(-1, len(image) + 1)]
    for y in range(-1, len(image) + 1):
        for x in range(-1, len(image[0]) + 1):
            new_image[y + 1][x + 1] = algorithm[neighbours(image, x, y, outside)]

    new_outside = '1' if algorithm[int(outside * 9, base=2)] == '#' else '0'
    
    return new_image, new_outside

for _ in range(2):
    image, outside = apply(image, algorithm, outside)

p1_sol = sum([sum([x == '#' for x in l]) for l in image])

for _ in range(48):
    image, outside = apply(image, algorithm, outside)

p2_sol = sum([sum([x == '#' for x in l]) for l in image])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
