# первый вариант
a = int(input('Введите целое положительное число n:'))
b = a*10+a
c = a*100+b
d = a+b+c
print(f'число n ={a}, сумма чисел n+nn+nnn={d}')
# второй вариант
a = input('Введите целое положительное число n:')
a1 = int(a)
b = int(a+a)
c = int(a+a+a)
e = a1+b+c
print(f'число n ={a}, сумма чисел n+nn+nnn={e}')