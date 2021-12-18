from aoc import AOC

aoc = AOC(25,  2020, __file__)

input = """
5764801
17807724
""".strip().split('\n')
input = aoc.input.strip().split('\n')

def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject
        value %= 20201227

    return value

card_pk, door_pk = map(int, input)

loop_size = 0
while pow(7, loop_size, 20201227) not in [card_pk, door_pk]:
    loop_size += 1

ecryption_key = pow(door_pk, loop_size, 20201227) if pow(7, loop_size, 20201227) == card_pk else pow(card_pk, loop_size, 20201227)

p1_sol = ecryption_key

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
