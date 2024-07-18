
cook_book = {}

with open('recipes.txt', 'r') as new_file:
    for line in new_file.readlines():
        line = line.replace('\n', '')
        try:
            int(line)
        except ValueError:
            if '|' not in line and line != '':
                bludo = line
                cook_book.update({bludo: []})
            elif line != '':
                line = line.split(' | ')
                cook_book[bludo].append({'ingredient_name': line[0], 'quantity': int(line[1]), 'measure': line[2]})


def get_shop_list_by_dishes(dishes: list, person_count: int):
    ingridient_dict = {}
    for dish in dishes:
        for ingr in cook_book.get(dish):
            if ingr['ingredient_name'] not in ingridient_dict.keys():
                ingridient_dict[ingr['ingredient_name']] = {'measure': ingr.get('measure'), 'quantity': ingr.get('quantity') * person_count}
            else:
                ingridient_dict[ingr['ingredient_name']]['quantity'] += ingr.get('quantity') * person_count

    return ingridient_dict


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))