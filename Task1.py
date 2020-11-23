# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']
    
    def start(self):
        i = 0
        while True:
            print(curent_light.__color[0])
            time.sleep(7)
            print(curent_light.__color[1])
            time.sleep(2)
            print(curent_light.__color[2])
            time.sleep(3)
            break
        print('Работа цикла завершена')


curent_light = TrafficLight()
curent_light.start()
