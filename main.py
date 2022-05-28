import os
import time
from pprint import pprint
from os import path

def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipe.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        for line in file_obj:
            dish_name = line.strip()
            count = int(file_obj.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = file_obj.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            file_obj.readline()
            cook_book[dish_name] = ing_list
    return cook_book
# pprint(read_cookbook())

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingredient_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingredient_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingredient_list[ings['ingredient_name']]['quantity'] = ingredient_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingredient_list



cook_book = read_cookbook()
print('Задача #1:')
pprint(cook_book)
time.sleep(3)
print('Задача #2:')
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))



