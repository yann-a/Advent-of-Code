from aoc import AOC

aoc = AOC(17,  2017, __file__)

input = 356

def part1():
    buffer = [0]
    skip = input
    current = 0
    for value in range(1, 2018):
        insert_pos = (current + skip) % len(buffer)
        
        buffer = buffer[:insert_pos + 1] + [value] + buffer[insert_pos + 1:]
        current = (insert_pos + 1) % len(buffer)

    return buffer[(current + 1) % len(buffer)]

def part2():
    skip = input
    current = 0
    current_length = 1
    last_1 = None
    for value in range(1, 50_000_001):
        insert_pos = (current + skip) % current_length
        if insert_pos == 0:
            last_1 = value
        current_length += 1
        current = (insert_pos + 1) % current_length

    return last_1


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
