from aoc import AOC

aoc = AOC(17,  2022, __file__)

input = aoc.input.strip().split('\n')[0]
#input = aoc.get_example(1).strip().split('\n')[0]

def part1():
    rocks = list(map(lambda rock: rock.split('\n')[::-1], open('rocks', 'r').read().strip().split('\n\n')))

    highest_rock = winds_id = 0
    rocks_map = ['#######']

    for rock_id in range(2022):
        rock = rocks[rock_id % len(rocks)]

        rock_height = len(rock)
        rock_width = len(rock[0])

        left, bottom = 2, highest_rock + 4
        while True:
            wind = input[winds_id % len(input)]
            dx = 1 if wind == '>' else -1
            if 0 <= left + dx <= 7 - rock_width:
                if all(
                    bottom + y not in range(len(rocks_map)) or rocks_map[bottom + y][left + dx + x] == '.'
                    for x in range(rock_width)
                    for y in range(rock_height)
                    if rock[y][x] == '#'
                    ):
                    left += dx
            winds_id += 1

            dy = -1
            if all(
                bottom + dy + y not in range(len(rocks_map)) or rocks_map[bottom + dy + y][left + x] == '.'
                for x in range(rock_width)
                for y in range(rock_height)
                if rock[y][x] == '#'
                ):
                bottom += dy
            else:
                for y in range(rock_height):
                    row = rocks_map[bottom + y] if bottom + y in range(len(rocks_map)) else '.' * 7
                    new_row = ''.join('#' if row[x] == '#' or (left <= x < left + rock_width and rock[y][x - left] == '#') else '.' for x in range(7))

                    if bottom + y in range(len(rocks_map)):
                        rocks_map[bottom + y] = new_row
                    else:
                        rocks_map.append(new_row)

                    highest_rock = max(highest_rock, bottom + y)
                break

    return highest_rock

def part2():
    rocks = list(map(lambda rock: rock.split('\n')[::-1], open('rocks', 'r').read().strip().split('\n\n')))

    highest_rock = winds_id = 0
    rocks_map = ['#######']

    seen = {}
    height, height_change = [0], [0]

    for rock_id in range(10_000):
        rock = rocks[rock_id % len(rocks)]

        rock_height = len(rock)
        rock_width = len(rock[0])

        left, bottom = 2, highest_rock + 4
        while True:
            wind = input[winds_id % len(input)]
            dx = 1 if wind == '>' else -1
            if 0 <= left + dx <= 7 - rock_width:
                if all(
                    bottom + y not in range(len(rocks_map)) or rocks_map[bottom + y][left + dx + x] == '.'
                    for x in range(rock_width)
                    for y in range(rock_height)
                    if rock[y][x] == '#'
                    ):
                    left += dx
            winds_id += 1

            dy = -1
            if all(
                bottom + dy + y not in range(len(rocks_map)) or rocks_map[bottom + dy + y][left + x] == '.'
                for x in range(rock_width)
                for y in range(rock_height)
                if rock[y][x] == '#'
                ):
                bottom += dy
            else:
                for y in range(rock_height):
                    row = rocks_map[bottom + y] if bottom + y in range(len(rocks_map)) else '.' * 7
                    new_row = ''.join('#' if row[x] == '#' or (left <= x < left + rock_width and rock[y][x - left] == '#') else '.' for x in range(7))

                    if bottom + y in range(len(rocks_map)):
                        rocks_map[bottom + y] = new_row
                    else:
                        rocks_map.append(new_row)

                highest_rock = max(highest_rock, bottom + rock_height - 1)
                height_change.append(max(0, highest_rock - height[-1]))
                height.append(highest_rock)
                break

    # slow, finds cycle length 1715 and starting pos 98
    # for the example: cycle length 35 and starting pos 16
    """
    for cycle_length in range(1, 5_000):
        for cycle_start in range(5_000):
            if all(height_change[cycle_start:cycle_start+cycle_length] == height_change[cycle_start+i*cycle_length:cycle_start+(i+1)*cycle_length] for i in range((len(height_change)-cycle_start)//cycle_length)):
                break
        else:
            continue
        break
    """

    cycle_start = 98
    #cycle_start = 16
    cycle_length = 1715
    #cycle_length = 35
    pos = 1_000_000_000_000

    start_cycle_height = height[cycle_start]
    cycle_height_change = sum(height_change[cycle_start+1:cycle_start+cycle_length+1])
    nb_full_cycles = (pos - cycle_start) // cycle_length
    additional_falls = (pos - cycle_start) % cycle_length

    final_height = start_cycle_height + cycle_height_change * nb_full_cycles + sum(height_change[cycle_start+1:cycle_start+additional_falls+1])

    return final_height

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
