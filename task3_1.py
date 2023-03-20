# вариант с list
class NewEx(Exception):
    pass


my_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
try:
    my_month = int(input('Введите номер месяца: '))
    if my_month < 1 or my_month > 12:
        raise NewEx
except NewEx:
    print('Введено не корректное значение')
    exit(0)
else:
    print(my_list[my_month - 1])
# вариант с dict
my_d = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
try:
    my_month = int(input('Введите номер месяца: '))
    if my_month < 1 or my_month > 12:
        raise NewEx
except NewEx:
    print('Введено не корректное значение')
    exit(0)
else:
    print(my_d[my_month])