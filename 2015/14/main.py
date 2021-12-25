from aoc import AOC

aoc = AOC(14,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

reindeers = []
for line in input:
    line = line.split()
    reindeers.append((int(line[3]), int(line[6]), int(line[13])))

def part1(reindeers, race_duration):
    def len_travelled(reindeer, time):
        speed, time_fly, time_rest = reindeer

        whole_cycles = time // (time_fly + time_rest)
        remaining_time = time % (time_fly + time_rest)
        additional_fly_time = min(time_fly, remaining_time)

        return speed * (time_fly * whole_cycles + additional_fly_time)

    return max(len_travelled(reindeer, race_duration) for reindeer in reindeers)

def part2(reindeers, race_duration):
    pos = [0 for _ in reindeers]
    flying = [True for _ in reindeers]
    clock = [0 for _ in reindeers]
    points = [0 for _ in reindeers]

    for second in range(race_duration):
        for i, reindeer in enumerate(reindeers):
            speed, time_fly, time_rest = reindeer

            if flying[i]:
                pos[i] += speed
                clock[i] += 1

                if clock[i] == time_fly:
                    clock[i] = 0
                    flying[i] = False
            else:
                clock[i] += 1

                if clock[i] == time_rest:
                    clock[i] = 0
                    flying[i] = True

        for i in range(len(reindeers)):
            if pos[i] == max(pos):
                points[i] += 1

    return max(points)

p1_sol = part1(reindeers, 2_503)
p2_sol = part2(reindeers, 2_503)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
