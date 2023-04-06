#Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
#length (длина в метрах), width (ширина в метрах).
#Значения данных атрибутов должны передаваться при создании экземпляра класса.
#Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
#всего дорожного полотна.

class Road:
    thickness = 0.05
    weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def my_method(self):
        res = self.thickness * self.weight * self._length * self._width
        return res

obj = Road(5000, 20)
b = obj.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')

# Рубрика "Эксперименты"
obj.thickness = 0.1
b = obj.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')

obj2 = Road(5000,20)
b = obj2.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')

Road.weight = 30
b = obj2.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')

b = obj.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')