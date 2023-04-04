from pprint import pprint

with open('recipies.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient, amount, unit = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient': ingredient,
                'amount': int(amount),
                'unit': unit
            })
        file.readline()
        cook_book[dish] = ingredients
    pprint(cook_book, sort_dicts=False, width=100)
# int(amount) is replacable with float(amount) to get fractions of measures
print("______________________________________________")

def get_shop_list_by_dishes(dishes, portions_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient'] not in shop_list:
                    shop_list[ingredient['ingredient']] = {
                        'amount': ingredient['amount'] * portions_count,
                        'unit': ingredient['unit']
                    }
                else:
                    if shop_list[ingredient['ingredient']]['unit'] == ingredient['unit']:
                        shop_list[ingredient['ingredient']]['amount'] += ingredient['amount'] * portions_count
                    else:
                        shop_list[ingredient['ingredient']]['amount'] = str(shop_list[ingredient['ingredient']]['amount'])\
                                                                        + shop_list[ingredient['ingredient']]['unit'] \
                                                                        + " + "\
                                                                        + str(ingredient['amount'] * portions_count) + \
                                                                        ingredient['unit']
                        shop_list[ingredient['ingredient']]['unit'] = "mixed"
        else:
            print(f"Мы не знаем как это готовить - {dish}")
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', "Каша", "Запеканка"], 2))






