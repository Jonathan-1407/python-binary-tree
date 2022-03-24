from os import system, name, path, getcwd
from .inputdata import getInputData, viewGeneratedInputData


def validateOption(message: str):
    try:
        option = input(message)
        return option
    except:
        print("** Valor invalido **")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def menu():
    print("==== Bienvenid@ ====")
    print("1 - Generar archivo con datos de entrada")
    print("2 - Generar archivo de salida")
    print("3 - Ver datos generados del archivo de entrada")
    print("4 - Ver datos ordenados del archivo de salida")
    print("5 - Salir")


option_menu = 0

while True:
    menu()

    option_menu = int(validateOption("Selecciona una opcion: "))

    if option_menu == 1:
        clear()

        print('\tDeseas ingresar la cantidad de datos a generar?')
        print('\tPresiona (enter) para omitir')
        length = validateOption(
            "\tIngresa la cantidad de datos, por defecto \033[93m100\033[0m: ")

        if length != "":
            getInputData(int(length))
        else:
            getInputData(100)

        clear()
        dir_path = path.abspath(getcwd())

        print('\033[92m\t === Archivo Generado ===\033[0m\n')
        print(
            '\tEl archivo se encuentra en: \n')
        print('\t\033[96m{}/public/files/Input.txt\033[0m\n'.format(dir_path))

    elif option_menu == 2:
        clear()
        print("Seleccionaste el archivo de salida\n")

    elif option_menu == 3:
        clear()
        viewGeneratedInputData()
    elif option_menu == 5:
        print('Ejecucion Finalizada')
        break
    else:
        clear()
        print("\n *** Opcion no valida ***\n")
