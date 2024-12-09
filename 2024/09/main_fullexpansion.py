from aoc import AOC

aoc = AOC(9,  2024, __file__)

input = aoc.input.strip().split('\n')[0]
#input = aoc.get_example(0).strip().split('\n')[0]

def part1():
    # Expand disk into an array
    s = []
    block_id = 0
    for i in range(0, len(input), 2):
        for j in range(int(input[i])): s.append(block_id)
        if i + 1 < len(input):
            for j in range(int(input[i + 1])): s.append('.')
        block_id += 1

    # Copy bytes from the back to the front one at a time
    dest_pointer = 0
    source_pointer = len(s) - 1
    while dest_pointer < source_pointer:
        while s[dest_pointer] != '.':
            dest_pointer += 1
    
        s[dest_pointer] = s[source_pointer]
        s[source_pointer] = '.'
        dest_pointer += 1
        
        while s[source_pointer] == '.':
            source_pointer -= 1

    # Compute checksum
    c = 0
    for i in range(len(s)):
        if s[i] != '.':
            c += i * s[i]

    return c

def part2():
    # Expand disk into an array + keep track of empty spans and files
    s = []
    free_spans = []
    files = []
    block_id = 0
    for i in range(0, len(input), 2):
        files.append((len(s), int(input[i])))
        for j in range(int(input[i])): s.append(block_id)
        if i + 1 < len(input):
            free_spans.append([len(s), int(input[i + 1])])
            for j in range(int(input[i + 1])): s.append('.')
        block_id += 1

    # Move each file into the first empty spans that fits
    for file in files[::-1]:
        pos, length = file

        pos_dest = [fs for fs in free_spans if fs[1] >= length]

        if len(pos_dest) == 0:
            continue

        dest = pos_dest[0]

        if dest[0] > pos:
            continue

        for i in range(length):
            s[dest[0] + i] = s[pos + i]
            s[pos + i] = '.'

        # If the span isn't entirely filled, we could still move a file there later
        if dest[1] > length:
            dest[0] += length
            dest[1] -= length
        else:
            free_spans = [span for span in free_spans if span != dest]

    # Compute checksum
    c = 0
    for i in range(len(s)):
        if s[i] != '.':
            c += i * s[i]

    return c

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
