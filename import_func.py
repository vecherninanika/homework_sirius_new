"""File where we import function."""

from project import readfile


while True:
    file_inp = input("Выберите файл - harry_potter.txt или avengers.txt (q чтобы выйти): ")
    if file_inp == 'q':
        break
    numberofstring = int(input('Введите номер от 1 до 7: '))
    print(readfile(file_inp, numberofstring))
