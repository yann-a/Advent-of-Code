from aoc import AOC

aoc = AOC(20,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

def part1():
    l = [(i, int(input[i])) for i in range(len(input))]
    uid_0 = [v[0] for v in l if v[1] == 0][0]
    prev = {}
    next = {}
    for i in range(len(l)):
        next[l[i]] = l[(i+1)%len(l)]
        prev[l[i]] = l[(i-1)%len(l)]

    for i in l:
        _, val = i
        if val == 0: continue

        j = i
        for _ in range(abs(val)):
            j = next[j] if val > 0 else prev[j]
        if val < 0: j = prev[j]

        next[prev[i]] = next[i]
        prev[next[i]] = prev[i]

        next[i] = next[j]
        prev[i] = j
        prev[next[j]] = i
        next[j] = i

    s, k = 0, (uid_0, 0)
    for _ in range(3):
        for _ in range(1000):
            k = next[k]
        s += k[1]
    
    return s

def part2():
    l = [(i, int(input[i]) * 811589153) for i in range(len(input))]
    uid_0 = [v[0] for v in l if v[1] == 0][0]
    prev = {}
    next = {}
    for i in range(len(l)):
        next[l[i]] = l[(i+1)%len(l)]
        prev[l[i]] = l[(i-1)%len(l)]

    for _ in range(10):
        for i in l:
            # Remove i from loop
            next[prev[i]] = next[i]
            prev[next[i]] = prev[i]

            # Move forwards
            j = prev[i]
            for _ in range(i[1] % (len(l) - 1)):
                j = next[j]

            # Reinsert i
            next[i] = next[j]
            prev[i] = j
            prev[next[j]] = i
            next[j] = i

    s, k = 0, (uid_0, 0)
    for _ in range(3):
        for _ in range(1000):
            k = next[k]
        s += k[1]
    
    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
