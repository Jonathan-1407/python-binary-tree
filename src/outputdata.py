def getDataFile():
    file = open('./public/files/Input.txt', 'r')
    print(file.read())
    file.close()

    return file


def getOutputData(order: int):
    if order == 1:
        getDataFile()
    elif order == 2:
        print('Nombres apellidos')
    elif order == 3:
        print('Carrera')
