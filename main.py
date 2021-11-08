# --------------------------------------------
import sys

from container import Container
from readStrArray import ReadStrArray

if __name__ == '__main__':
    inputFileName = ""
    output1FileName = ""
    output2FileName = ""
    container = Container()
    # Должно быть ровно 7 значений в массиве:
    # 0) Полный путь к main.py
    # 1) python
    # 2) main.py
    # 3) -n или -f
    # 4) путь к inputFile или количество элементов в контейнере
    # 5) путь к outputFile1
    # 6) путь к outputFile2
    if len(sys.argv) == 7:
        if sys.argv[3] == "-f":
            inputFileName = sys.argv[4]
            output1FileName = sys.argv[5]
            output2FileName = sys.argv[6]
            print('==>Start')
            # Чтените исходного файла, содержащего данные, разделённые пробелами и переводами строки
            iFile = open(inputFileName)
            string = iFile.read()
            iFile.close()
            strArray = string.replace("\n", " ").split(" ")
            # Формирование массива строк
            filmsNumber = ReadStrArray(container, strArray)
        elif sys.argv[3] == "-n":
            if 10000 >= int(sys.argv[4]) > 0:
                filmsNumber = int(sys.argv[4])
                output1FileName = sys.argv[5]
                output2FileName = sys.argv[6]
                # Заполнение контейнера случайными данными
                container.InRnd(filmsNumber)
                print('==>Start')
    else:
        print("Incorrect command line! You must write: python main -f <inputFileName> <output1FileName>\n"
              "<output2FileName> OR python main -n <number> <output1FileName> <output2FileName>")
        exit()

    # Тестовый вывод содержимого контейнера
    container.Print()

    # Вывод содержимого контейнера в первый файл
    oFile1 = open(output1FileName, 'w')
    container.Write(oFile1)

    # Сортировка контейнера
    container.Sort()

    # Вывод отсортированного содержимого контейнера во второй файл
    oFile2 = open(output2FileName, 'w')
    container.Write(oFile2)
    oFile1.close()
    oFile2.close()

    print('==>Finish')
