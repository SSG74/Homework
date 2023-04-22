class IsString:

    def __set__(self, prop, value):
        if type(value) == int:
            raise ValueError("Не может быть числовым")

        prop.__dict__[self.my_attr] = value
    def __set_name__(self, rank, my_attr):
        self.my_attr = my_attr
class NonNegative:
        def __set__(self, prop, value):
            if value < 0:
                raise ValueError("Не может быть отрицательным")

            prop.__dict__[self.my_attr] = value
        def __set_name__(self, rank, my_attr):
            self.my_attr = my_attr


class Worker:
    name = IsString()
    surname = IsString()
    wage = NonNegative()
    bonus = NonNegative()
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.bonus = bonus
       # self.income = {'wage':wage, 'bonus':bonus}
    def get_full_name(self):
        return self.name + ' ' + self.surname
#
    def get_total_income(self):
        return self.wage + self.bonus
#
person = Worker('Иван', 'Петров', 30000, 10000)

print(person.get_full_name())
print(f'доход: {person.get_total_income()}')

person.name = 'Олег'
person.surname = 'Иванов'
person.wage = 20000
person.bonus = 30000
print(person.get_full_name())
print(f'доход: {person.get_total_income()}')