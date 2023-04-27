# Задание 2.
#
# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.
#
# Подсказки:
# --- b'class' - используйте маркировку b''
# --- используйте списки и циклы, не дублируйте функции

one_wld = 'class'
two_wld = 'function'
three_wld = 'method'

def str_unc(wld):
    chrs = list(wld)
    #print(chrs)
    el = ''
    for i in chrs:
        el = el + rf"{ord(i):02x}"
    return el


for j in one_wld, two_wld, three_wld:
    a = str_unc(j)

    print(j)
    print(a)
    print(len(a), "байт")
    print(bytes(j, 'utf-8'))
print(chr(int('6d', 16)))

m_str = 'class'
print(m_str.encode())

