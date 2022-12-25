from aoc import AOC

aoc = AOC(25,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

snafu_digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
digits_snafu = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

def snafu_to_decimal(number):
    s, r = 0, 1
    for i in range(len(number)):
        s += snafu_digits[number[len(number) - i - 1]] * r
        r *= 5

    return s

def decimal_to_snafu(number):
    r, i = '', 0
    while number > 0:
        if number % 5 <= 2:
            r += digits_snafu[number % 5]
            number //= 5
        else:
            r += digits_snafu[(number % 5) - 5]
            number = (number + 5)// 5
        i += 1

    return r[::-1]

def part1():
    return decimal_to_snafu(sum(snafu_to_decimal(number) for number in input))

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
