instructions = [line.split(' ') for line in open('input', 'r')]

pos, depth, aim = 0, 0, 0
for instruction in instructions:
    if instruction[0] == 'forward':
        pos += int(instruction[1])
        depth += aim * int(instruction[1])
    if instruction[0] == 'down':
        aim += int(instruction[1])
    if instruction[0] == 'up':
        aim -= int(instruction[1])

print('Part 1:', pos * aim)
print('Part 2:', pos * depth)
