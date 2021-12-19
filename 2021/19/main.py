from aoc import AOC

aoc = AOC(19,  2021, __file__)

#input = aoc.get_example(5).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

def parse_input(input):
    scanners = {}
    for scanner_data in input:
        lines = scanner_data.split('\n')

        scanner_id = int(lines[0][12:-4])
        beacon_pos = []
        for beacon in lines[1:]:
            coords = beacon.split(',')
            beacon_pos.append((int(coords[0]), int(coords[1]), int(coords[2])))

        scanners[scanner_id] = beacon_pos
    
    return scanners

def rotate2d(coords):
    rotate_0 = coords[:]
    rotate_90 = list(map(lambda c: (c[0], -c[2], c[1]), coords))
    rotate_180 = list(map(lambda c: (c[0], -c[1], -c[2]), coords))
    rotate_270 = list(map(lambda c: (c[0], c[2], -c[1]), coords))

    return [rotate_0, rotate_90, rotate_180, rotate_270]

def rotate(coords):
    face1up_rots = rotate2d(coords)
    face1down_rots = rotate2d(list(map(lambda c: (-c[0], c[2], c[1]), coords)))

    face2up_rots = rotate2d(list(map(lambda c: (c[1], c[2], c[0]), coords)))
    face2down_rots = rotate2d(list(map(lambda c: (-c[1], c[0], c[2]), coords)))

    face3up_rots = rotate2d(list(map(lambda c: (c[2], c[0], c[1]), coords)))
    face3down_rots = rotate2d(list(map(lambda c: (-c[2], c[1], c[0]), coords)))

    face_rots = [face1up_rots, face1down_rots, face2up_rots, face2down_rots, face3up_rots, face3down_rots]

    return [rot for face_rot in face_rots for rot in face_rot]

scanners = parse_input(input)

real_coords = {}
real_coords[0] = scanners[0]
scanners_pos = []
while len(real_coords) < len(scanners):
    for s in scanners:
        inter, Dx, Dy, Dz = False, 0, 0, 0
        if s not in real_coords:
            s_rots = rotate(scanners[s])
            for s_rot in s_rots:
                for placed_s in real_coords:
                    c1_coord = set(real_coords[placed_s])
                    for c1 in real_coords[placed_s]:
                        for c2 in s_rot:
                            dx, dy, dz = c1[0] - c2[0], c1[1] - c2[1], c1[2] - c2[2]
                            c2_coords_1 = set()
                            for c2_coord in s_rot:
                                c2_coords_1.add((c2_coord[0] + dx, c2_coord[1] + dy, c2_coord[2] + dz))
                            
                            if len(c1_coord.intersection(c2_coords_1)) >= 12:
                                inter = True
                                Dx, Dy, Dz = dx, dy, dz
                                break
                        if inter:
                            s_coords = []
                            for c in s_rot:
                                s_coords.append((c[0] + Dx, c[1] + Dy, c[2] + Dz))
                            real_coords[s] = s_coords
                            scanners_pos.append((Dx, Dy, Dz))
                            break
                    if inter:
                        break
                if inter:
                    break
            if inter:
                break
        if inter:
            break

beacons = set()
for s in real_coords:
    beacons = beacons.union(set(real_coords[s]))

max_man_dist = 0
for c1 in scanners_pos:
    for c2 in scanners_pos:
        max_man_dist = max(max_man_dist, abs(c2[0] - c1[0]) + abs(c2[1] - c1[1]) + abs(c2[2] - c1[2]))

p1_sol = len(beacons)
p2_sol = max_man_dist

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
