from aoc import AOC
import hashlib

aoc = AOC(5,  2016, __file__)

input = 'ugkcyxxp'

door_id = input
nonce = 0
part1_password = ''
part2_password = list('........')
len_p2_password = 0
while len(part1_password) < 8 or len_p2_password < 8:
    h = hashlib.md5()
    h.update(door_id.encode())
    h.update(str(nonce).encode())
    hash = h.hexdigest()

    if hash[:5] == '00000':
        if len(part1_password) < 8:
            part1_password += hash[5]
        
        if hash[5] not in 'abcdef' and 0 <= int(hash[5]) < 8 and part2_password[int(hash[5])] == '.':
            part2_password[int(hash[5])] = hash[6]
            len_p2_password += 1

    nonce += 1

p1_sol = part1_password
p2_sol = ''.join(part2_password)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
