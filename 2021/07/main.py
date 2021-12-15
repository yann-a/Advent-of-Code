pos = [int(p) for p in open('input').readline().split(',')]

minpos = min(pos)
maxpos = max(pos)

print('Part 1:', min([sum([abs(moy - p) for p in pos]) for moy in range(minpos, maxpos + 1)]))
print('Part 2:', min([sum([abs(moy - p)*(abs(moy - p) + 1) // 2 for p in pos]) for moy in range(minpos, maxpos + 1)]))
