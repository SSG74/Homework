class NonNegative:
    def __set__(self, prop, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")

        prop.__dict__[self.my_attr] = value

    def __set_name__(self, rank, my_attr):
        self.my_attr = my_attr

class Road:
    thickness = 0.05
    weight = 25
    length = NonNegative()
    width = NonNegative()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def my_method(self):
        res = self.thickness * self.weight * self._length * self._width
        return res

obj = Road(5000, 20)
b = obj.my_method()
print(f'Масса асфальта для покрытия дороги - {int(b)} кг или {int(b)/1000} тонн')


obj.length = 4000
obj.width = -25
print(obj.my_method())