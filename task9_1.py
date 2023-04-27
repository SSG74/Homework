class NonNegative:

    # def __init__(self, my_attr):
    #     self.my_attr = my_attr

    # def __get__(self, prop, rank):
    #
    #     return prop.__dict__[self.my_attr]

    def __set__(self, prop, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")

        prop.__dict__[self.my_attr] = value

    # def __delete__(self, prop):
    #     del prop.__dict__[self.my_attr]

    def __set_name__(self, rank, my_attr):
        self.my_attr = my_attr



class Worker:

    hours = NonNegative()#'hours')
    rate = NonNegative()#'rate')

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate

Obj = Worker('Степан', 'Петров', 8, 150)
print(Obj.total_profit())

Obj.hours = 10
Obj.rate = -200
# print(Obj.__dict__)
print(Obj.total_profit())
