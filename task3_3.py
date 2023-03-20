# задаем словари
one_d = {'название':'компьютер', 'цена':40000, 'количество':6, 'ед.':'шт.'}
two_d = {'название':'принтер', 'цена':20000, 'количество':3, 'ед.':'шт.'}
three_d = {'название':'сканер', 'цена':15000, 'количество':4, 'ед.':'шт.'}
# создаем кортежи
one_tup = (1, one_d)
two_tup = (2, two_d)
three_tup = (3, three_d)
# one_tup = (1, {'название':'компьютер', 'цена':40000, 'количество':6, 'ед.':'шт.'})
# two_tup = (2, {'название':'принтер', 'цена':20000, 'количество':3, 'ед.':'шт.'})
# three_tup = (3, {'название':'сканер', 'цена':15000, 'количество':4, 'ед.':'шт.'})
# создаем список Товары
products = [(one_tup), (two_tup), (three_tup)]
# выводим построчно списки
# for i in products:
#     print(i)
print('Продукты:')
print(products)
# создаем списки значений по ключас
one_l = [one_d.get('название'), two_d.get('название'), three_d.get('название')]
#print(one_l)
two_l = [one_d.get('цена'), two_d.get('цена'), three_d.get('цена')]
#print(two_l)
three_l = [one_d.get('количество'), two_d.get('количество'), three_d.get('количество')]
#print(three_l)
four_l = [one_d.get('ед.'), two_d.get('ед.'), three_d.get('ед.')]
# удаляем повторы из 4-го списка
del four_l[1:3]
#print(four_l)
# создаем итоговый словарь со списками значений
five_d = {'название':one_l, 'цена':two_l, 'количество':three_l, 'ед.':four_l}
# выводим построчно пары "ключ:значения"
# for item in five_d:
#     print('{}:{}'.format(item,five_d[item]))
print('Словарь:')
print(five_d)