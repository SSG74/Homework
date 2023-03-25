from timeit import timeit
from random import randint

list_1 = list()
n = 0
for i in range(0, n):
    x = randint(0, 100)
    list_1.append(x)

print(timeit("list()",globals=globals()), "seconds")