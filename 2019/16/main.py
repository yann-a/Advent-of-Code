from aoc import AOC

aoc = AOC(16,  2019, __file__)

input = aoc.input.strip()

BASE_PATTERN =  [0, 1, 0, -1]
LEN_PRECALC = len(input)
PATTERN = [[BASE_PATTERN[((j + 1) // (i + 1)) % len(BASE_PATTERN)]  for j in range(LEN_PRECALC)] for i in range(LEN_PRECALC)]

def fft(input_fft):
    v = ''
    for i in range(len(input_fft)):
        r = sum(PATTERN[i][j] * int(input_fft[j]) for j in range(len(input_fft)))
        v += str(abs(r) % 10)
    return v

def part1():
    r = input
    for _ in range(100):
        r = fft(r)

    return r[:8]   

def part2():
    offset = int(input[:7])
    input_fft = (input * 10_000)[offset:]

    for _ in range(100):
        s = 0
        r_fft = ''
        for index in range(len(input_fft)-1, -1, -1):
            s += int(input_fft[index])
            r_fft += str(abs(s) % 10)

        input_fft = r_fft[::-1]

    return input_fft[:8]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
