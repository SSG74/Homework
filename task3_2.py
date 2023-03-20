rating = [11,9,8,6,5,5,3,1]
print(rating)
el = int(input('введите натуральное число: '))
# добавляем новое число в конец списка
rating.append(el)
print(rating)
# сортируем список по возрастанию значений
rating.sort()
print(rating)
# разворачиваем список - по убыванию
rating.reverse()
print(rating)