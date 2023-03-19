from random import randint

n = int(input('Введите число монет:'))
count_zero = 0
count_one = 0
for i in range(n):
    x = randint(0, 1)
    print(x)
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f'минимальное число монеток - {count_zero}')
else:
    print(f'минимальное число монеток - {count_one}')