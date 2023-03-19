s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(x, y)