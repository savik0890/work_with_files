
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
