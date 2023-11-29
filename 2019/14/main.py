from aoc import AOC
from collections import defaultdict
from math import ceil

aoc = AOC(14,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(4).strip().split('\n')

def produce(product, quantity, recipies, stock):
    if product == 'ORE': return quantity

    missing_quantity = quantity - stock[product]
    if missing_quantity <= 0:
        stock[product] -= quantity
        return 0

    product_qty, ingredients = recipies[product]
    needed_recp_qty = ceil(missing_quantity / product_qty)

    stock[product] = stock[product] + product_qty * needed_recp_qty - quantity

    s = 0
    for ingredient_qty, ingredient in ingredients:
        s += produce(ingredient, int(ingredient_qty) * needed_recp_qty, recipies, stock)

    return s

def part1():
    recipies = {}
    for line in input:
        ingredients, product = line.split(' => ')
        ingredients = [ingredient.split() for ingredient in ingredients.split(', ')]
        product = product.split()

        recipies[product[1]] = (int(product[0]), ingredients)

    return produce('FUEL', 1, recipies, defaultdict(int))

def part2(p1_sol):
    recipies = {}
    for line in input:
        ingredients, product = line.split(' => ')
        ingredients = [ingredient.split() for ingredient in ingredients.split(', ')]
        product = product.split()

        recipies[product[1]] = (int(product[0]), ingredients)

    ORE = 1_000_000_000_000

    low = high = 1
    while produce('FUEL', high, recipies, defaultdict(int)) < ORE:
        low = high
        high *= 2

    while low < high:
        mid = (low + high) // 2
        ore = produce('FUEL', mid, recipies, defaultdict(int))
        if ore < ORE: low = mid + 1
        elif ore > ORE: high = mid - 1
        else: break
    
    while produce('FUEL', mid, recipies, defaultdict(int)) <= ORE:
        mid += 1

    return mid - 1

p1_sol = part1()
p2_sol = part2(p1_sol)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#&aoc.submit(2, p2_sol)
