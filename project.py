"""Main project file."""


def readfile(file_inp: str, numberofstring: int) -> str:
    """Shows the name of the movie of the chosen file and number.

    Args:
        file_inp(str): file with movies in order 1-7
        numberofstring(int): number of the movie (1-7)

    Returns:
        str: name of the chosen movie

    """
    try:
        with open(file_inp) as file_input:
            return file_input.readlines()[numberofstring - 1]
    except FileNotFoundError:
        return 'Нет такого файла'
    except IndexError:
        return 'Вы ввели неправильный номер'
