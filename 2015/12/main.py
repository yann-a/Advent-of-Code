from aoc import AOC
import json

aoc = AOC(12,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

js = json.loads(input[0])

def intopt(s):
    try:
        return int(s)
    except:
        return 0

def containsred(el):
    if isinstance(el, dict):
        return any([k == 'red' or el[k] == 'red' for k in el])
    
    return False

def browse1(el):
    if isinstance(el, list):
        return sum([browse1(e) for e in el])
    elif isinstance(el, dict):
        return sum([intopt(k) + browse1(el[k]) for k in el])
    else:
        return intopt(el)

def browse2(el):
    if isinstance(el, list):
        return sum([browse2(e) for e in el])
    elif isinstance(el, dict):
        if containsred(el):
            return 0

        return sum([intopt(k) + browse2(el[k]) for k in el])
    else:
        return intopt(el)

p1_sol = browse1(js)
p2_sol = browse2(js)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
