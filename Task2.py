# Реализовать класс Road (дорога),
# в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    __length = 20
    __width = 5000

    def mass_full(self, base_mas, base_tall):
        """Функция ждет два параметро:
        mass_full(масса квадратногометра толщиной 1см, толщина слоя)"""
        print('Масса всего полотна:', (Road.__length * Road.__width * base_mas * base_tall) / 1000, 'тон')


mass = Road()
mass.mass_full(25, 5)
