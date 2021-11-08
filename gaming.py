# --------------------------------------------
from film import Film
from rnd import RandomInt
from rnd import RandomString


class Gaming(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def ReadStrArray(self, strArray, i):
        # Проверка на конец чтения
        if i >= len(strArray) - 1:
            return 0

        # Получение значения названия фильма и года выхода
        self.name = strArray[i]
        self.year = int(strArray[i + 1])

        # Получение значения длительности документального фильма
        self.director = strArray[i + 2]
        i += 3
        return i

    # Случайный ввод данных игрового фильма
    def GetRandomInfo(self):
        rnd2000 = RandomInt(1000, 2000)
        rndFilmName = RandomString("film name")
        rndDirectorName = RandomString("director name")
        self.name = rndFilmName.Get()
        self.year = rnd2000.Get()
        self.director = rndDirectorName.Get()

    # Вывод данных игрового фильма в консоль
    def Print(self):
        super().Print()
        print("It is a gaming film. Director: ", self.director, ".\n")
        pass

    # Вывод данных игрового фильма в файл
    def Write(self, oStream):
        super().Write(oStream)
        oStream.write("It is a gaming film. Director: {}.\n".format(self.director))
        pass
