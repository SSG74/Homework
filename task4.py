income = int(input('Введите значение выручки, рублей: '))
expense = int(input('Введите значение расходов, рублей: '))
if income > expense:
    print("фирма работала с прибылью")
    profit = (income - expense)/income
    print(f'Рентабельность выручки: {profit}')
else:
    print("фирма работала с убытком")

numbers = int(input('Введите численность сотрудников: '))
print(f'Прибыль на одного сотрудника: {(income - expense)/numbers} рублей')