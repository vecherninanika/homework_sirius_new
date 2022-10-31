
from project import readfile
while True:
    file = input("Выберите файл - harry_potter.txt или avengers.txt (q чтобы выйти): ")
    if file == 'q':
        break
    numberofstring = int(input('Введите номер от 1 до 7: '))
    print(readfile(file, numberofstring))
