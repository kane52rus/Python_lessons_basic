# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
lass Worker:
    def __init__(self, name, surname, money, position, hours):
        self.name = name
        self.surname = surname
        self.money = int(money)
        self.position = position
        self.hours = int(hours)
        self.work_hours = 0


    def read_hours_of(self):
        with open("data/hours_of", "r", encoding="UTF-8") as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.work_hours = int(i.split()[2])
                    break
                else:
                    continue

    def calc_money(self):
        per_hour = self.money // self.hours
        if self.work_hours > self.hours:
            return (((self.work_hours - self.hours) * per_hour) * 2) + self.money
        elif self.work_hours < self.hours:
            return self.work_hours * per_hour
        else:
            return self.money

    def write_money(self, money):
        with open('ZUP.txt', 'a', encoding='UTF-8') as f:
            f.write(self.name + ' ' + self.surname + ' ' + str(money) + ' ' + self.position)
            f.write('\n')


def file_handle(file):
    f = open(file, 'r', encoding='UTF-8')
    for i in f.readlines():
        if i.count('Имя') == 1:
            continue
        else:
            # обработка строки
            name, surname, money, position, norm_hours = i.split()
            workman = Worker(name, surname, money, position, norm_hours)
            workman.read_hours_of()
            money = workman.calc_money()
            workman.write_money(money)
    f.close()


file_handle("data/workers")
