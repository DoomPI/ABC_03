class Film:
    def __init__(self):
        self.year = 0
        self.name = ""

    # Вывод данных фильма в консоль
    def Print(self):
        print("This is a film named \"", self.name, "\". It was produced in ",
              self.year, " year.\nThe quotient equals ", self.Quotient())
        pass

    # Вывод данных фильма в файл
    def Write(self, oStream):
        oStream.write(
            "This is a film named \"{}\". It was produced in {} year.\n"
            "The quotient equals {}\n".format(self.name, self.year, self.Quotient()))
        pass

    # Подсчёт частного года выхода и длины строки-названия фильма
    def Quotient(self):
        return self.year / len(self.name)
        pass
