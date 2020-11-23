# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = ''
    surname = ''
    position = 'дровосек'
    _income = {"wage": 1000, "bonus": 500}


class Position(Worker):

    def get_full_name(self):
        print('из класса Position', self.name, self.surname)

    def get_total_income(self):
         print('Зарплата:', self._income.get('wage'), 'Премия:', self._income.get('bonus'))
         print('Общий доход', sum(self._income.values()))


Worker.name = input('Имя: ')
Worker.surname = input('Фамилия: ')

worker_origin = Worker()
print('из класса Worker', worker_origin.name, worker_origin.surname)

worker_position = Position()
worker_position.get_full_name()
worker_position.get_total_income()
