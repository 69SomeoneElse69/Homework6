# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
import time


class Car:
    _speed = 100
    _color = 'non'
    _name = 'non'
    _is_police = bool
    direction = 'non'

    def go(self):
        print('Движение вперед')

    def stop(self):
        print('Остановка машины')

    def turn(direction):
        print('Движение', direction.direction)

    def show_speed(self):
        print('Скорость:', self._speed, 'автомобиля', self._name)

# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class SportCar(Car):
    def __init__(self, name, color, speed, police, direction):
        self._name = name
        self._color = color
        self._speed = int(speed)
        self._is_police = bool(police)
        self.direction = direction

class TownCar(Car):
    def __init__(self, name, color, speed, police, direction):
        self._name = name
        self._color = color
        self._speed = int(speed)
        self._is_police = bool(police)
        self.direction = direction


    def show_speed(self):
        if self._speed > 60:
            print('Скорость:', self._speed, 'Превышение скорости', self._name, 'на', self._speed - 60)
        else:
            print('скорость TownCar', self._speed)


class WorkCar(Car):
    def __init__(self, name, color, speed, police, direction):
        self._name = name
        self._color = color
        self._speed = int(speed)
        self._is_police = bool(police)
        self.direction = direction

    def show_speed(self):
        if self._speed > 40:
            print('Скорость:', self._speed, 'Превышение скорости', self._name, 'на', self._speed - 40)
        else:
            print('скорость WorkCar', self._speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed, police, direction):
        self._name = name
        self._color = color
        self._speed = int(speed)
        self._is_police = bool(police)
        self.direction = direction


# Создайте экземпляры классов, передайте значения атрибутов.
car1 = SportCar('SportCar', 'Желтый', 200, False, 'лево')
car2 = TownCar('TownCar', 'Белый', 100, False, 'право')
car3 = WorkCar('WorkCar', 'Зеленый', 39, False, 'разворот')
car4 = PoliceCar('PoliceCar', 'Специальный', 170, True, 'взлет!')

# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
print('Значения атрибутов базового класса:')
print(Car._speed)
print(Car._color)
print(Car._name)
print(Car._is_police)
print(Car.direction)
time.sleep(3)

print('======================================================\n' * 2)
print('Значения атрибутов базового дочернего класса SportCar:')
print(car1._speed)
print(car1._color)
print(car1._name)
print(car1._is_police)
print(car1.direction)
time.sleep(3)

print('======================================================')
print('Выдолнение методов базового дочернего класса SportCar:')
car1.go()
time.sleep(1)
car1.show_speed()
time.sleep(1)
car1.turn()
time.sleep(1)
car1.stop()

time.sleep(1)
print('========next========')
time.sleep(1)

print('Значения атрибутов базового дочернего класса TownCar:')
print(car2._speed)
print(car2._color)
print(car2._name)
print(car2._is_police)
time.sleep(3)

print('======================================================')
print('Выдолнение методов базового дочернего класса TownCar:')
car2.go()
time.sleep(1)
car2.show_speed()
time.sleep(1)
car2.turn()
time.sleep(1)
car2.stop()
#
time.sleep(1)
print('========next========')
time.sleep(1)

print('Значения атрибутов базового дочернего класса WorkCar:')
print(car3._speed)
print(car3._color)
print(car3._name)
print(car3._is_police)
time.sleep(3)

print('======================================================')
print('Выдолнение методов базового дочернего класса WorkCar:')
car3.go()
time.sleep(1)
car3.show_speed()
time.sleep(1)
car3.turn()
time.sleep(1)
car3.stop()

time.sleep(1)
print('========next========')
time.sleep(1)

print('Значения атрибутов базового дочернего класса PoliceCar:')
print(car4._speed)
print(car4._color)
print(car4._name)
print(car4._is_police)
time.sleep(3)

print('======================================================')
print('Выдолнение методов базового дочернего класса PoliceCar:')
car4.go()
time.sleep(1)
car4.show_speed()
time.sleep(1)
car4.turn()
time.sleep(1)
car4.stop()
