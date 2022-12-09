from aoc import AOC

aoc = AOC(8,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    visible = set()

    for i in range(len(input)):
        maxv = -1
        for j in range(len(input[0])):
            if int(input[i][j]) > maxv:
                visible.add((i, j))
                maxv = int(input[i][j])

    for i in range(len(input)):
        maxv = -1
        for j in range(len(input[0])-1, -1, -1):
            if int(input[i][j]) > maxv:
                visible.add((i, j))
                maxv = int(input[i][j])


    for j in range(len(input[0])):
        maxv = -1
        for i in range(len(input)):
            if int(input[i][j]) > maxv:
                visible.add((i, j))
                maxv = int(input[i][j])

    for j in range(len(input[0])):
        maxv = -1
        for i in range(len(input)-1, -1, -1):
            if int(input[i][j]) > maxv:
                visible.add((i, j))
                maxv = int(input[i][j])

    return len(visible)

def part2():
    max_sceninc_score = 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            d = []

            for ni in range(i-1, -1, -1):
                if int(input[ni][j]) >= int(input[i][j]):
                    d.append(i - ni)
                    break
            else:
                d.append(i)
                
            for ni in range(i+1, len(input)):
                if int(input[ni][j]) >= int(input[i][j]):
                    d.append(ni - i)
                    break
            else:
                d.append(len(input) - i - 1)

            for nj in range(j-1, -1, -1):
                if int(input[i][nj]) >= int(input[i][j]):
                    d.append(j  - nj)
                    break
            else:
                d.append(j)

            for nj in range(j+1, len(input[0])):
                if int(input[i][nj]) >= int(input[i][j]):
                    d.append(nj - j)
                    break
            else:
                d.append(len(input[0]) - j - 1)

            if i == 1 and j == 2:
                print(d)

            max_sceninc_score = max(max_sceninc_score, d[0] * d[1] * d[2] * d[3])

    return max_sceninc_score


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
