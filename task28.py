a = int(input('Введите число а = '))
b = int(input('Введите число b = '))

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)
print(f'сумма чисел: {summa(a,b)}')