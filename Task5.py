# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', self.title)

# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen', self.title)


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки Pencil', self.title)

class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки Handle', self.title)

# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
user_pan = Pen('Оглавление')
user_pan.draw()

user_pan2 = Pen('Заголовок')
user_pan2.draw()

user_penc = Pencil('Прописные')
user_penc.draw()

user_penc2 = Pencil('Строчные')
user_penc2.draw()

user_handle = Handle('Выделение')
user_handle.draw()

user_handle2 = Handle('Пометки')
user_handle2.draw()
