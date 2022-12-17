from aoc import AOC

aoc = AOC(15,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    wrong_pos = set()
    beacons = set()
    for line in input:
        line = line.split()
        sx, sy = int(line[2][2:-1]), int(line[3][2:-1])
        bx, by = int(line[8][2:-1]), int(line[9][2:])

        md = abs(sx - bx) + abs(sy - by)
        y = 2_000_000
        for x in range(sx - md, sx + md + 1):
            if sy - (md - abs(sx - x)) <= y <= sy + (md - abs(sx - x)):
                if (x, y) not in beacons:
                    wrong_pos.add((x, y))

        beacons.add((bx, by))
        if (bx, by) in wrong_pos:
            wrong_pos.remove((bx, by))
    
    return len(wrong_pos)

def part2():
    sensors = set()
    beacons = set()
    for line in input:
        line = line.split()
        sx, sy = int(line[2][2:-1]), int(line[3][2:-1])
        bx, by = int(line[8][2:-1]), int(line[9][2:])
        md = abs(sx - bx) + abs(sy - by)

        sensors.add((sx, sy, md))
        beacons.add((bx, by))

    for sx, sy, md in sensors:
        just_outside = set()
        for x in range(sx - md, sx + md + 1):
            if 0 <= x <= 4_000_000:
                if 0 <= sy - (md - abs(sx - x)) - 1 <= 4_000_000: just_outside.add((x, sy - (md - abs(sx - x)) - 1))
                if 0 <= sy + (md - abs(sx - x)) + 1 <= 4_000_000: just_outside.add((x, sy + (md - abs(sx - x)) + 1))
        if 0 <= sx - md - 1 <= 4_000_000 and 0 <= sy <= 4_000_000: just_outside.add((sx - md - 1, sy))
        if 0 <= sx + md + 1 <= 4_000_000 and 0 <= sy <= 4_000_000: just_outside.add((sx + md + 1, sy))

        for x, y in just_outside:
            if all(abs(nsx - x) + abs(nsy - y) > nmd for nsx, nsy, nmd in sensors):
                return x * 4_000_000 + y

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
