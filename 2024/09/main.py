from aoc import AOC

aoc = AOC(9,  2024, __file__)

input = list(map(int, list(aoc.input.strip().split('\n')[0])))
#input = list(map(int, list(aoc.get_example(0).strip().split('\n')[0])))

def part1():
    data = input[:]

    dest_pointer = dest_id = 0
    source_pointer = len(data) - 1

    nb_blocks = len(data) // 2 + 1
    dest_block_id, source_block_id = 0, nb_blocks - 1

    s = 0
    while dest_pointer <= source_pointer:
        # Compute checksum for fixed values
        for i in range(data[dest_pointer]):
            s += dest_block_id * dest_id
            dest_id += 1
        dest_block_id += 1
        dest_pointer += 1

        if dest_pointer > source_pointer:
            break

        # Push end values into the empty spaces
        nb_vals_sum = 0
        while nb_vals_sum < data[dest_pointer]:
            nb_vals = min(data[dest_pointer] - nb_vals_sum, data[source_pointer])
            nb_vals_sum += nb_vals
            for i in range(nb_vals):
                s += source_block_id * dest_id
                dest_id += 1

            if nb_vals == data[source_pointer]:
                source_pointer -= 2
                source_block_id -= 1
            else:
                data[source_pointer] -= nb_vals

            if dest_pointer > source_pointer:
                break

        dest_pointer += 1

    return s

def part2():
    data = input[:]

    dest_pointer = dest_id = 0
    source_pointer = len(data) - 1

    nb_blocks = len(data) // 2 + 1
    dest_block_id, source_block_id = 0, nb_blocks - 1

    files = []

    # Compute files positions and upper checkbound sum
    s = position = block_id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            files.append((position, data[i], block_id))
            for j in range(data[i]): s += block_id * (position + j)
            block_id += 1

        position += data[i]

    # For each empty position, look for a file to place there and update checksum accordingly
    position = 0
    files = files[::-1]
    to_pop = []
    for i in range(len(data)):
        if i % 2 == 1:
            nb_vals_sum = 0
            for j, f in enumerate(files):
                if f[1] <= data[i] - nb_vals_sum and position + nb_vals_sum < f[0]:
                    s += f[2] * (position + nb_vals_sum - f[0]) * f[1]
                    nb_vals_sum += f[1]

                    to_pop.append(j)

                if nb_vals_sum == data[i]:
                    break

            # Remove moved files from list
            for j in to_pop[::-1]:
                files.pop(j)
            to_pop = []

        position += data[i]

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
