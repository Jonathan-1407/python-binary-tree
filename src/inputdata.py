from os import getenv
from dotenv import load_dotenv
import random

load_dotenv()


# M -> Male or F -> Female
def generateNames(gender: str, route_file: str, word_length: int):
    tmp_names = []

    fns = open(
        route_file, "r")

    for i in fns.readlines():
        if gender == "":
            tmp_names.append(i.strip('\n'))
        else:
            if f"-{gender}" in i.strip('\n'):
                tmp_names.append(i.strip('\n').replace(f"-{gender}", ''))
            else:
                continue

    fns.close()
    if word_length == 2:
        names = "{} {}".format(
            random.choice(tmp_names), random.choice(tmp_names))
    else:
        names = "{}".format(random.choice(tmp_names))
    return names


def generateCardId(length: int):
    num = ''.join(random.choice('0123456789') for i in range(length))
    return num


def viewGeneratedInputData():
    file = open(getenv('FILE_INPUT_PATH'), 'r')
    print(file.read())
    file.close()


def generateData(length: int, gender: str):
    students = []
    mixed_length = int(length / 2)
    gender = 'F'

    for i in range(length):
        card_id = f"{generateCardId(5)}-{generateCardId(2)}-{generateCardId(5)}"
        first_names = generateNames(
            f"{gender}", getenv('FILE_FIRST_NAMES_PATH'), 2)
        last_names = generateNames(
            "", getenv('FILE_LAST_NAMES_PATH'), 2)
        university_course = generateNames(
            "", getenv('FILE_UNIVERSITY_COURSES_PATH'), 1)

        full_student = "{}|{}|{}|{};\n".format(
            card_id, first_names, last_names, university_course).upper()

        if i == mixed_length:
            gender = 'M'

        students.append(full_student)

    return students


def getInputData(length: int = 100, gender: str = 'MIXED'):
    file = open(getenv('FILE_INPUT_PATH'), 'w')
    students = generateData(length, gender)
    random.shuffle(students)

    for student in students:
        file.write(student)

    file.close()
