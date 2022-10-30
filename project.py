def readfile(file, numberofstring):
        try:
            with open(file) as file:
                return file.readlines()[numberofstring-1]
        except FileNotFoundError:
            return 'Нет такого файла'
        except IndexError:
            return 'Вы ввели неправильный номер'


