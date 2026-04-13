print("Grilled Cheese Sandwhich")

servings = int(input("How many servings?"))

ingredients = {
    'Slices of bread': 2,
    'Slices of cheese': 3,
    'Tablespoons of butter': 2,
    'Cups of Soup': 1.5
}
total_ingredients={}

print(ingredients)
for ingredient in ingredients:
    quantity = ingredients[ingredient]
    total_quantity = quantity*servings
    total_ingredients[ingredient] = total_quantity
    print(f'{quantity*servings} {ingredient}')

print(total_ingredients)