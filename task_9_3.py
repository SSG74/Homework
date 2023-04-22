 #Дз метод Синглтон
class TypedMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyClass(metaclass=TypedMeta):
    def method_1(self):
        pass
    def method_2(self):
        print("Небольшая проблема")

obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)