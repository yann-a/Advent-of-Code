from aoc import AOC

aoc = AOC(8,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    boxes = [tuple(map(int, line.split(','))) for line in input]
    distances = [
        [
            (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2 for p in boxes
        ] for q in boxes
    ]
    flat_distances = [(distances[ip][iq], ip, iq) for ip in range(len(boxes)) for iq in range(ip)]
    flat_distances.sort()
    flat_distances = flat_distances[:1000]

    circuits = []
    for d, ip, iq in flat_distances:
        pc = pq = None
        for ic, c in enumerate(circuits):
            if ip in c:
                pc = ic
            if iq in c:
                pq = ic
        
        if pc is not None and pq is not None and pc != pq:
            circuits[pc] |= circuits[pq]
            circuits.pop(pq)
        elif pc is not None:
            circuits[pc].add(iq)
        elif pq is not None:
            circuits[pq].add(ip)
        else:
            circuits.append(set([ip, iq]))

    r = 1
    for c in sorted(circuits, key=len,reverse=True)[:3]:
        r *= len(c)

    return r

def part2():
    boxes = [tuple(map(int, line.split(','))) for line in input]
    distances = [
        [
            (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2 for p in boxes
        ] for q in boxes
    ]
    flat_distances = [(distances[ip][iq], ip, iq) for ip in range(len(boxes)) for iq in range(ip)]
    flat_distances.sort()

    circuits = []
    connected = []
    for d, ip, iq in flat_distances:
        pc = pq = None
        for ic, c in enumerate(circuits):
            if ip in c:
                pc = ic
            if iq in c:
                pq = ic

        if not(pc is not None and pq is not None and pc == pq):
            connected.append((ip, iq))
        
        if pc is not None and pq is not None and pc != pq:
            circuits[pc] |= circuits[pq]
            circuits.pop(pq)
        elif pc is not None:
            circuits[pc].add(iq)
        elif pq is not None:
            circuits[pq].add(ip)
        else:
            circuits.append(set([ip, iq]))

    ip, iq = connected[-1]
    return boxes[ip][0] * boxes[iq][0]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
