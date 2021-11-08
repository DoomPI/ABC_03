# --------------------------------------------
from film import Film
from type import DrawingType
from rnd import RandomInt
from rnd import RandomString


class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.type = 0

    def ReadStrArray(self, strArray, i):
        # Проверка на конец чтения
        if i >= len(strArray) - 1:
            return 0

        # Получение значения названия фильма и года выхода
        self.name = strArray[i]
        self.year = int(strArray[i + 1])

        # Получение значения метода рисовки мультфильма
        filmType = int(strArray[i + 2])
        if filmType == 1:
            self.type = DrawingType.drawn
        elif filmType == 2:
            self.type = DrawingType.stop_motion
        elif filmType == 3:
            self.type = DrawingType.plasticine
        i += 3
        return i

    # Случайный ввод данных мультфильма
    def GetRandomInfo(self):
        rnd3 = RandomInt(1, 3)
        rnd2000 = RandomInt(1000, 2000)
        rndFilmName = RandomString("film name")
        self.name = rndFilmName.Get()
        self.year = rnd2000.Get()
        filmType = rnd3.Get()
        if filmType == 1:
            self.type = DrawingType.drawn
        elif filmType == 2:
            self.type = DrawingType.stop_motion
        elif filmType == 3:
            self.type = DrawingType.plasticine

    # Вывод данных мультфильма в консоль
    def Print(self):
        super().Print()
        if self.type == DrawingType.drawn:
            print("It is a cartoon. It was created by using drawn method.\n")
        elif self.type == DrawingType.stop_motion:
            print("It is a cartoon. It was created by using stop motion method.\n")
        elif self.type == DrawingType.plasticine:
            print("It is a cartoon. It was created by using plasticine method.\n")
        pass

    # Вывод данных мультфильма в файл
    def Write(self, oStream):
        super().Write(oStream)
        if self.type == DrawingType.drawn:
            oStream.write("It is a cartoon. It was created by using drawn method.\n")
        elif self.type == DrawingType.stop_motion:
            oStream.write("It is a cartoon. It was created by using stop motion method.\n")
        elif self.type == DrawingType.plasticine:
            oStream.write("It is a cartoon. It was created by using plasticine method.\n")
        pass
