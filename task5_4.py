n = int(input('введите число n: '))
def get_sum(lst_el):
    el = 1
    get_sum = 0

    if len(lst_el) == 1:
        return lst_el[0]
    get_sum += el
    el /= -2
    return lst_el[0] + get_sum(lst_el[1:n])
print(f'сумма {n} элементов ряда чисел равна {get_sum}')