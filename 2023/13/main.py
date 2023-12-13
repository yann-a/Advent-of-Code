from aoc import AOC

aoc = AOC(13,  2023, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    s = 0
    for pattern in input:
        grid = pattern.split('\n')
        
        for line in range(len(grid) - 1):
            k = 0
            isref = True
            while 0 <= line - k and line + k + 1 < len(grid):
                if grid[line - k] != grid[line + k + 1]:
                    isref = False
                    break
                k += 1
            
            if isref:
                s += 100 * (line + 1)
                break
        
        if isref:
            continue

        for col in range(len(grid[0]) - 1):
            k = 0
            isref = True
            while 0 <= col - k and col + k + 1 < len(grid[0]):
                if any(grid[i][col - k] != grid[i][col + k + 1] for i in range(len(grid))):
                    isref = False
                    break
                k += 1
            
            if isref:
                s += col + 1
                break

    return s

def part2():
    s = 0
    for pattern in input:
        grid = pattern.split('\n')

        isFound = False
        for line in range(len(grid) - 1):
            k = 0
            nbe = 0
            while 0 <= line - k and line + k + 1 < len(grid):
                for i in range(len(grid[0])):
                    if grid[line - k][i] != grid[line + k + 1][i]:
                        nbe += 1
                k += 1
            
            if nbe == 1:
                s += 100 * (line + 1)
                isFound = True
                break
        
        if isFound:
            continue

        for col in range(len(grid[0]) - 1):
            k = 0
            nbe = 0
            while 0 <= col - k and col + k + 1 < len(grid[0]):
                for i in range(len(grid)):
                    if grid[i][col - k] != grid[i][col + k + 1]:
                        nbe += 1
                k += 1
            
            if nbe == 1:
                s += col + 1
                break

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
