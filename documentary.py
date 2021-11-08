# --------------------------------------------
from film import Film
from rnd import RandomInt
from rnd import RandomString


class Documentary(Film):
    def __init__(self):
        super().__init__()
        self.length = 0

    def ReadStrArray(self, strArray, i):
        # Проверка на конец чтения
        if i >= len(strArray) - 1:
            return 0

        # Получение значения названия фильма и года выхода
        self.name = strArray[i]
        self.year = int(strArray[i + 1])

        # Получение значения длительности документального фильма
        self.length = int(strArray[i + 2])
        i += 3
        return i

    # Случайный ввод данных документального фильма
    def GetRandomInfo(self):
        rnd180 = RandomInt(100, 180)
        rnd2000 = RandomInt(1000, 2000)
        rndFilmName = RandomString("film name")
        self.name = rndFilmName.Get()
        self.year = rnd2000.Get()
        self.length = rnd180.Get()

    # Вывод данных документального фильма в консоль
    def Print(self):
        super().Print()
        print("It is a documentary. Length: ", self.length, " minutes.\n")
        pass

    # Вывод данных документального фильма в файл
    def Write(self, oStream):
        super().Write(oStream)
        oStream.write("It is a documentary. Length: {} minutes.\n".format(self.length))
        pass
