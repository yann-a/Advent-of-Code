from aoc import AOC

aoc = AOC(8,  2015, __file__)

input = """
\"\"
\"abc\"
\"aaa\\\"aaa\"
\"\\x27\"
""".strip().split('\n')
input = aoc.input.strip().split('\n')

def part1():
    code_len = content_len = 0
    for string in input:
        code_len += len(string)
        content_len += (len(string)
            - 3 * string.count('\\x')
            + 3 * string.count('\\\\x')
            - 3 * string.count('\\\\\\x')

            - string.count('\\\\')

            - string.count('\\\"')
            + string.count('\\\\\"')
            - string.count('\\\\\\\"')

            - 2)

    return code_len - content_len

def part2():
    code_len = content_len = 0
    for string in input:
        content_len += len(string)
        code_len += (len(string) + string.count('\"') + string.count('\\') + 2)

    return code_len - content_len

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
