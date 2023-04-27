#Задание 3.
#
# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" исключение,
# придумайте как это сделать


one_wrd = 'attribute'
two_wrd = 'класс'
three_wrd = 'функция'
four_wrd = 'type'
def str_unc(wrd):
    chrs = list(wrd)
    can_convert = True

    for i in chrs:
        if ord(i) > 127:
            can_convert = False
            break
    return can_convert
for j in one_wrd, two_wrd, three_wrd, four_wrd:
    a = str_unc(j)
    if a:
        print(j, 'можно перевести в байты')
    else:
        print(j, 'нельзя перевести в байты')
