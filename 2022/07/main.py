from aoc import AOC
from collections import defaultdict

aoc = AOC(7,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def parse_graph():
    pile = []
    graph = defaultdict(set)
    sizes = defaultdict(int)

    i = 0
    while i < len(input):
        ls = input[i].split()

        if ls[1] == 'cd':
            if ls[2] == '/':
                pile = ['/']
            elif ls[2] == '..':
                pile.pop(-1)
            else:
                pile.append(ls[2])

            i += 1

        elif ls[1] == 'ls':
            i += 1

            while i < len(input) and not input[i].startswith('$'):
                taille, nom = input[i].split()
                full_path = '-'.join(pile)

                graph[full_path].add(full_path + '-' + nom)
                if taille != 'dir':
                    sizes[full_path + '-' + nom] = int(taille)

                i += 1

    return graph, sizes

def compute_sizes(graph, sizes, dir_sizes, current_folder):
    score = size = 0
    for e in graph[current_folder]:
        if e in sizes:
            sc, si = 0, sizes[e]
        else:
            sc, si = compute_sizes(graph, sizes, dir_sizes, e)

        score += sc
        size += si

    dir_sizes[current_folder] = size
    if size <= 100_000:
        score += size

    return score, size

def part1():
    graph, sizes = parse_graph()

    dir_sizes = defaultdict(int)
    return compute_sizes(graph, sizes, dir_sizes, '/')[0]

def part2():
    graph, sizes = parse_graph()

    dir_sizes = defaultdict(int)
    compute_sizes(graph, sizes, dir_sizes, '/')

    unused_space = 70_000_000 - dir_sizes['/']
    needed_space = 30_000_000 - unused_space

    return min(dir_sizes[s] for s in dir_sizes if dir_sizes[s] >= needed_space)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
