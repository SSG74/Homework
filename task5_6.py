from random import randint
num = randint(0, 100)
print(num)
m = int(input('назовите число: '))
def get_fun(num, m):

    if num == m:
        return (num)
print(f'вы отгадали число {num}')
    #return get_fun(num, m)
if (m - num) > 0:
    print('загаданное число меньше')
if (m - num) < 0:
    print('загаданное число больше')
def recursive_counter(m):
    recursive_counter = 0
    recursive_counter += 1
    if recursive_counter(m) >= 10:
       return
    print('попытки отгадывания числа закончились')

