from aoc import AOC
import hashlib

aoc = AOC(4,  2015, __file__)

input = "bgvyzdsv"

def mine(secret, nb_zeros):
    nonce = 1
    while True:
        h = hashlib.md5()
        h.update(secret.encode())
        h.update(str(nonce).encode())
        
        hexdigest = h.hexdigest()
        if hexdigest[:nb_zeros] == "0" * nb_zeros:
            return nonce

        nonce += 1

p1_sol = mine(input, 5)
p2_sol = mine(input, 6)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
