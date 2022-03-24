from os import system, name, path, getcwd
from .inputdata import getInputData, viewGeneratedInputData
from .outputdata import getOutputData


def drawWelcome():
    print("▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ 　 ▀█▀ ▀█▀ ▀█▀")
    print("▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ▒█░▄▄ ▒█▄▄▀ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ 　 ▒█░ ▒█░ ▒█░")
    print("▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ 　 ▄█▄ ▄█▄ ▄█▄")
    print("")


def drawEndExcecution():
    print("+-----------------------------------------+")
    print("|                                         |")
    print("|        \033[35m** Ejecucion Finalizada **\033[0m       |")
    print("|                                         |")
    print("+-----------------------------------------+")


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


drawWelcome()


def menu():
    print("==== Bienvenid@ ====")
    print("1 - Generar archivo con datos de entrada")
    print("2 - Generar archivo de salida")
    print("3 - Ver datos generados del archivo de entrada")
    print("4 - Ver datos ordenados del archivo de salida")
    print("5 - Salir")


def outputMenu():
    print("\t==== Ordernar por? ====")
    print("\t1 - Carne")
    print("\t2 - Nombres y apellidos")
    print("\t3 - Carrera\n")

    option = validateOption(
        "\tIngresa una opcion, por defecto \033[93mCarne\033[0m: ")

    return option


option_menu = 0

while True:
    try:
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
            print(
                '\t\033[96m{}/public/files/Input.txt\033[0m\n'.format(dir_path))

        elif option_menu == 2:
            clear()
            output_option = outputMenu()

            if output_option == "1" or output_option == "2" or output_option == "3":
                clear()
                getOutputData(int(output_option))
            else:
                clear()
                output_option = 1
                getOutputData(output_option)

        elif option_menu == 3:
            clear()
            viewGeneratedInputData()
        elif option_menu == 5:
            clear()
            drawEndExcecution()
            break
        else:
            clear()
            print("\n *** Opcion no valida ***\n")
    except:
        clear()
        print("** Ingresa un valor valido **")
