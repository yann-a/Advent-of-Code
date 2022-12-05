from aoc import AOC

aoc = AOC(3,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')


def part1():
    s = 0
    for line in input:
        for c in line[:len(line)//2]:
            if c in line[len(line)//2:]:
                if c.islower():
                    s += ord(c) - ord('a') + 1
                else:
                    s += ord(c) - ord('A') + 27
                break
            else:
                continue
            break
    return s

def part2():
    s = 0
    for i in range(0, len(input), 3):
        s1 = set(input[i])
        s2 = s1.intersection(set(input[i+1]))
        s3 = s2.intersection(set(input[i+2]))

        for c in s3:
            if c.islower():
                s += ord(c) - ord('a') + 1
            else:
                s += ord(c) - ord('A') + 27
    
    return s


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)