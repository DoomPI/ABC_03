# --------------------------------------------
from cartoon import Cartoon
from documentary import Documentary
from gaming import Gaming
from rnd import RandomInt


class Container:
    def __init__(self):
        self.storage = []

    # Случайный ввод содержимого контейнера
    def InRnd(self, filmsNumber):
        rnd3 = RandomInt(1, 3)
        length = 0
        while length < filmsNumber:
            key = rnd3.Get()
            if key == 1:
                film = Cartoon()
                film.GetRandomInfo()
                self.storage.append(film)
            if key == 2:
                film = Documentary()
                film.GetRandomInfo()
                self.storage.append(film)
            if key == 3:
                film = Gaming()
                film.GetRandomInfo()
                self.storage.append(film)
            length += 1
    pass

    # Вывод содержимого контейнера в консоль
    def Print(self):
        print("Container stores", len(self.storage), "films:")
        for film in self.storage:
            film.Print()
        pass

    # Вывод содержимого контейнера в файл
    def Write(self, oStream):
        oStream.write("Container stores {} films:\n".format(len(self.storage)))
        for film in self.storage:
            film.Write(oStream)
            oStream.write("\n")
        pass

    # Подсчёт среднего арифметического частных всех элементов контейнера
    def AverageQuotient(self):
        average_quotient = 0.0
        for film in self.storage:
            average_quotient += film.Quotient()
        return average_quotient / len(self.storage)

    # Простейшая сортировка выбором
    def Sort(self):
        for film in self.storage:
            if film.Quotient() > self.AverageQuotient():
                self.storage.append(self.storage.pop(self.storage.index(film)))
