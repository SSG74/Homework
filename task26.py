

a = float(input('Введите число а = '))
b = int(input('Введите число b = '))
#c = b // 1
def pow(a,b):
    if b == 0:
        return 1
    return a * pow(a, b - 1)
print(f'результат возведения числа {a} в целую степень {b} -> {pow(a,b)}')
