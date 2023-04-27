# Задание 4.
#
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции


one_wrd = 'разработка'
two_wrd = 'администрирование'
three_wrd = 'protocol'
four_wrd = 'standard'
for j in one_wrd, two_wrd, three_wrd, four_wrd:
    print(j)
    d = j.encode('unicode_escape')
    print(d)
    print(d.decode('unicode_escape'))
