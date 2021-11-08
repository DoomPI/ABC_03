from cartoon import Cartoon
from documentary import Documentary
from gaming import Gaming


def ReadStrArray(container, strArray):
    arrayLength = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    filmsNumber = 0
    while i < arrayLength:
        string = strArray[i]
        key = int(string)  # Преобразование в целое
        if key == 1:  # Признак мультфильма
            i += 1
            film = Cartoon()
            i = film.ReadStrArray(strArray, i)
        elif key == 2:  # Признак документального фильма
            i += 1
            film = Documentary()
            i = film.ReadStrArray(strArray, i)
        elif key == 3:  # Признак игрового фильма
            i += 1
            film = Gaming()
            i = film.ReadStrArray(strArray, i)
        else:
            # Что-то пошло не так. Должен быть известный признак
            # Вовзрат количества прочитанных фильмов
            return filmsNumber
        if i == 0:
            return filmsNumber
        filmsNumber += 1
        container.storage.append(film)
    return filmsNumber
