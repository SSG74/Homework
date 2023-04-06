#Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}
class Position(Worker):
      def __init__(self,  name, surname, position, wage, bonus):
         super().__init__(name, surname, position, wage, bonus)

      def get_full_name(self):
          return self.name + ' ' + self.surname

      def get_total_income(self):
          return self._income.get('wage') + self._income.get('bonus')

person = Position('Иван', 'Петров', 'вахтер', 30000, 10000)

print(person.get_full_name())
print(person.position)
print(f'доход: {person.get_total_income()}')