from random import randint
n = int(input('n= '))

list_1 = list()
for i in range(n):
    x = randint(0, 30)
    list_1.append(x)
print(list_1)
list_1_count = list()
for i in range(len(list_1) - 1):
    list_1_count.append(list_1[i-1] + list_1[i] + list_1[i+1])

list_1_count.append(list_1[-2] + list_1[-1] + list_1[0])
print(max(list_1_count))
