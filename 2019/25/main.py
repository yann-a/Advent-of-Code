from aoc import AOC
from intcode import *
from itertools import combinations

aoc = AOC(25,  2019, __file__)

input_str = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

all_dirs = ['north', 'east', 'south', 'west']

def readOutput(intcode, items_to_take):
    _output = ''
    while len(intcode.output) > 0:
        _output += chr(intcode.getOutput())
    output = _output.strip().split('\n\n')

    place_name = output[0].split('\n')[0][3:-3]
    items, dirs = [], []

    for el in output[1:]:
        el = el.split('\n')
        if el[0].startswith('Items'):
            for item in el[1:]:
                item = item[1:].strip()
                items.append(item)
        elif el[0].startswith('Doors'):
            for item in el[1:]:
                item = item[1:].strip()
                dirs.append(item)

    done = place_name == 'Pressure-Sensitive Floor' and 'ejected' not in _output
    if done:
        print(items_to_take)
        print(_output.strip())

    return place_name, items, dirs

def sendASCIIInput(intcode, dir):
    for c in dir + '\n':
        intcode.addInput(ord(c))

def explore(intcode, prevdir, items_dir, all_prev_dirs, seen, items_to_take):
    intcode.run()
    place_name, items, dirs = readOutput(intcode, items_to_take)

    if place_name not in seen:
        seen[place_name] = all_prev_dirs

        items_dir[place_name] = items
        for item in items:
            if item in items_to_take:
                sendASCIIInput(intcode, 'take ' + item)
                intcode.run()
                readOutput(intcode, items_to_take)

        for dir in dirs:
            if prevdir is None or dir != all_dirs[(all_dirs.index(prevdir) + 2) % 4]:
                sendASCIIInput(intcode, dir)
                explore(intcode, dir, items_dir, all_prev_dirs + [dir], seen, items_to_take)

    if prevdir is not None:
        sendASCIIInput(intcode, all_dirs[(all_dirs.index(prevdir) + 2) % 4])
        intcode.run()
        readOutput(intcode, items_to_take)

def free_exploration():
    program = list(map(int, input_str[0].split(',')))
    intcode = IntCodeProgram(program)

    while True:
        intcode.run()

        while len(intcode.output) > 0:
            print(chr(intcode.getOutput()), end='')

        for c in input() + '\n':
            intcode.addInput(ord(c))

def part1():
    program = list(map(int, input_str[0].split(',')))

    # Explore to get full floor map
    """
    items = defaultdict(set)
    seen = {}

    intcode = IntCodeProgram(program)
    explore(intcode, None, items, [], seen)
    for el in seen:
        print(el, seen[el], items[el])
    """

    # Explore by hand to find all items that make you lose
    # free_exploration()

    # Then for all possible combinations of items, find the one that makes you enter the pressure sensor room
    possible_items = set(['asterisk', 'astronaut ice cream', 'hologram', 'fixed point', 'ornament', 'antenna', 'dark matter', 'monolith'])
    for nb_items in range(len(possible_items)+1):
        all_items_to_take = combinations(possible_items, nb_items)

        for items_to_take in all_items_to_take:
            items = defaultdict(set)
            seen = {}
            intcode = IntCodeProgram(program)
            explore(intcode, None, items, [], seen, items_to_take)

    # Read code in stdout
    return 134227456

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
