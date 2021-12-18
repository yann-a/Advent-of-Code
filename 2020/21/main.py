from aoc import AOC

aoc = AOC(21,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

all_ingredients = []
allergens_can_be_in = {}

for line in input:
    ingredients, allergens = line.strip(')\n').split(' (contains ')
    ingredients = ingredients.split()
    allergens = allergens.split(', ')

    all_ingredients += ingredients
    for allergen in allergens:
        if allergen in allergens_can_be_in:
            allergens_can_be_in[allergen] &= set(ingredients)
        else:
            allergens_can_be_in[allergen] = set(ingredients)

potentially_contain_allergens = set([ingredient for allergen in allergens_can_be_in for ingredient in allergens_can_be_in[allergen]])
safe_ingredients = [ingredient for ingredient in all_ingredients if ingredient not in potentially_contain_allergens]

danger_list = {}
while len(danger_list) < len(allergens_can_be_in):
    for ingredient in allergens_can_be_in:
        if len(allergens_can_be_in[ingredient]) == 1:
            for el in allergens_can_be_in[ingredient]:
                danger_list[ingredient] = el
            for other_ingredient in allergens_can_be_in:
                try:
                    allergens_can_be_in[other_ingredient].remove(el)
                except:
                    pass

danger_list = [(alergen, danger_list[alergen]) for alergen in danger_list]
danger_list.sort()

p1_sol = len(safe_ingredients)
p2_sol = ','.join([el[1] for el in danger_list])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
