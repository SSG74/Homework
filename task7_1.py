# задача 1
# время красного сигнала 7 секунд
# время желтого сигнала 2 секунды
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    def running(self, time_green):
        print(f'горит {self.__color[0]}')
        sleep(7)
        print(f'горит {self.__color[1]}')
        sleep(2)
        print(f'горит {self.__color[2]}')
        sleep(time_green)

time_3 = float(input('введите время зеленого сигнала: '))

from time import sleep

color = TrafficLight()
print(f'светофор включен')
color.running(time_3)
print(f'светофор отключен')







