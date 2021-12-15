from aoc import AOC

aoc = AOC(7,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

graph = {}

for line in input:
    bag, contents = line.split(' bags contain ')
    graph[bag] = []

    if contents == 'no other bags.':
        continue

    contents = contents.split(', ')
    for content in contents:
        nb = int(content.split()[0])
        color = ' '.join(content.split()[1:3])

        graph[bag].append((color, nb))


def can_contain(color):
    colors = set([t[0] for t in graph[color]])
    for neighbor in graph[color]:
        colors = colors.union(can_contain(neighbor[0]))
    return colors


def must_contain(color):
    nb = 0
    for neighbor in graph[color]:
        nb += neighbor[1]*(1 + must_contain(neighbor[0]))
    return nb


p1_sol = sum([1 if 'shiny gold' in can_contain(c) else 0 for c in graph])
p2_sol = must_contain('shiny gold')

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
