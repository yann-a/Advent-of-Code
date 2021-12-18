from aoc import AOC

aoc = AOC(18,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def explode(number):
    depth = cursor = 0
    while True:
        if cursor >= len(number):
            return number
        elif number[cursor] == '[':
            depth += 1
            cursor += 1
        elif number[cursor] == ']':
            depth -= 1
            cursor += 1
        elif depth >= 5:
            comma_pos = cursor
            while number[comma_pos] != ',':
                comma_pos += 1

            closing_pos = comma_pos
            while number[closing_pos] != ']':
                closing_pos += 1

            try:
                lv = int(number[cursor:comma_pos])
                rv = int(number[comma_pos + 1:closing_pos])
            except:
                cursor += 1
                continue

            # Explode on the left
            left_left, left_right = cursor - 2, cursor - 1
            while left_right >= 0 and (number[left_right] != ']' or number[left_right - 1] == ']') and (number[left_right] != ',' or number[left_right - 1] == ']'):
                left_left -= 1
                left_right -= 1
            while left_left >= 0 and number[left_left] != ',' and number[left_left] != '[' :
                left_left -= 1

            if left_left >= 0:
                new_left_part = number[:cursor - 1][:left_left + 1] + str(int(number[left_left + 1:left_right]) + lv) + number[:cursor - 1][left_right:]
            else:
                new_left_part = number[:cursor - 1]

            # Explode on the right
            right_left, right_right = closing_pos + 1, closing_pos + 2
            while right_left < len(number) and (number[right_left] != '[' or number[right_left + 1] == '[') and (number[right_left] != ',' or number[right_left + 1] == '['):
                right_left += 1
                right_right += 1
            while right_right < len(number) and number[right_right] != ',' and number[right_right] != ']':
                right_right += 1

            if right_right < len(number):
                new_right_part = number[closing_pos + 1:right_left + 1] + str(int(number[right_left + 1: right_right]) + rv) + number[right_right:]
            else:
                new_right_part = number[closing_pos + 1:]

            return new_left_part + '0' + new_right_part
        else:
            cursor += 1

def split(number):
    cursor = 0
    while cursor < len(number):
        if number[cursor] in '0123456789':
            fin_nb = cursor + 1
            while number[fin_nb] in '0123456789':
                fin_nb += 1

            nb = int(number[cursor:fin_nb])

            if nb >= 10:
                nb_l = nb//2
                nb_r = nb//2 if nb % 2 == 0 else nb//2 + 1

                return number[:cursor] + "[" + str(nb_l) + "," + str(nb_r) + "]" + number[fin_nb:]

        cursor += 1

    return number

def reduce(number):
    while True:
        old_number = number

        while True:
            new_explode_number = explode(number)

            if new_explode_number == number:
                break

            number = new_explode_number

        number = split(number)

        if old_number == number:
            return number

    

def magnitude(number):
    if number[0] in '0123456789':
        return int(number)
    
    depth = 0
    for cursor in range(len(number)):
        if number[cursor] == '[': depth += 1
        elif number[cursor] == ']': depth -= 1
        elif number[cursor] == ',' and depth == 1: return 3 * magnitude(number[1:cursor]) + 2 * magnitude(number[cursor + 1: -1])

# Part 1 : sum all and compute magnitude
number = input[0]
for num in input[1:]:
    number = reduce(f'[{number},{num}]')
p1_sol = magnitude(number)

# Part 2 : sum all pairs and pick max magnitude
max_magnitude = 0
for n1 in input:
    for n2 in input:
        if n1 != n2:
            max_magnitude = max(max_magnitude, magnitude(reduce(f'[{n1},{n2}]')))
p2_sol = max_magnitude

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
