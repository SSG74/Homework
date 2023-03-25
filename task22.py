from random import randint

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
list_1 = list()
for i in range(0, n):
    x = randint(0, 100)
    list_1.append(x)
list_2 = list()
for i in range(0, m):
    x = randint(0,100)
    list_2.append(x)
print(list_1)
print(list_2)
set_1 = set(list_1)
set_2 = set(list_2)
#print(set_1)
#print(set_2)
set_3 = set_1.intersection(set_2)
#print(set_3)
list_3 = list(set_3)
#print(list_3)
#list_4 = list_3.sort()
#print(list_4)
#print(len(list_4))
if len(list_3) < 1:
    print('нет совпадений')
else:
    print(sorted(list_3))


