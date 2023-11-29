from aoc import AOC

aoc = AOC(8,  2019, __file__)

input = aoc.input.strip().split('\n')[0]
#input = aoc.get_example(0).strip().split('\n')

def part1():
    nb_layers = len(input) // (25 * 6)
    layers = [input[layer*25*6:(layer+1)*25*6] for layer in range(nb_layers)]    

    most_0_layer = min(layers, key=lambda layer: layer.count('0'))
    return most_0_layer.count('1') * most_0_layer.count('2')

def part2():
    nb_layers = len(input) // (25 * 6)
    layers = [input[layer*25*6:(layer+1)*25*6] for layer in range(nb_layers)]    

    for line in range(6):
        for x in range(25):
            for layer in layers:
                if layer[line*25+x] != '2':
                    print('#' if layer[line*25+x] == '1' else ' ', end='')
                    break
        print()

p1_sol = part1()
part2()
p2_sol = 'KFABY'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
