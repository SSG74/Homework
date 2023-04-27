# class Meta(type):
#     @classmethod
#     def __prepare__(cls, clsname, bases):
#         print('>> Meta. __prepare__', cls, clsname, bases)
#         return dict()
#
#     def __new__(cls, clsname, bases, clsdict):
#
#
#  # второй пример
#
# class NewClass(type):
#     def __new__(cls, name, bases, dict):
#         new_class = super(NewClass, cls).__new__(cls, name, bases, dict)
#         print(name)
#         print(bases)
#         print(dict)
#         return new_class
#
# class Parent_1:
#     pass
# # делаем свой метакласс
# class MyClass(Parent_1, metaclass=NewClass):
#     pass
#
# obj = MyClass
#
#
#
#
# #к примеру 4
# class DocMeta(type):
#
#     def __init__(self, clsname, bases, clsdict):
# #или new
#         print(clsdict.items())
#         for key, value in clsdict.items():
#             # пропустить любые спец и частные методы
#             if key.startswith("__"):
#                 continue
#             #пропустить любые невызываемые объекты
#             if not hasattr(value, "__call__"):
#                 continue
#
#             #проверка наличия действия
#             if not getattr(value, "__doc__"):
#                 raise TypeError(f'Метод {key} должен иметь строку документации')
#
#         type.__init__(self, clsname, bases, clsdict)
#
# #пример 4
# class MyClass(metaclass=DocMeta):
#
#     def method_1(self):
#
#         pass
#
#     def method_2(self):
#         print("Небольшая проблема")
#
# mc = MyClass()
#
#
# # пример 3
# class MyMetaClass(type):
#     # должен вернуть словарь для атрибутов класса
#     @classmethod
#     def __prepare__(metacls, name, bases):
#         print('Перегружаю prepare')
#         return type.__prepare__(metacls, name, bases)
#
# #должен создать и вернуть новый класс
#     def __new__(cls, name, bases, dct):
#         print(f'Выделение памяти для класса {name},' f'имеющего кортеж базовых классов {bases}'f' и словарь атрибутов {dct}')
#         return type.__prepare__(cls, name, bases, dct)
#     #должен инициализировать созданный класс
#         def __init__(cls, name, bases, dct):
#             print(f'Инициализация класса {name}')
#             super(MyMetaClass, cls).__init__(name, bases, dct)
#             # должен создать и вернуть экземпляр нового класса
#         def __call__(self, *arg, **kwargs):
#             print('Перегружаю call')
#             return type.__call__(self, *arg, **kwargs)
