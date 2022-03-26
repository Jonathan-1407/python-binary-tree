from .binarytree import BinarySearchTree, getTreeData
from os import getenv
from dotenv import load_dotenv


def viewOrderedOutputData():
    file = open(getenv('FILE_OUTPUT_PATH'), 'r')
    print(file.read())
    file.close()


def getDataFile():
    students = []

    file = open(getenv('FILE_INPUT_PATH'), 'r')
    file_total_lines = file.readlines()
    for student in file_total_lines:
        students.append(student.strip())

    file.close()

    return students


def getOutputData(order: int):
    available_order = [1, 2, 3]
    if order not in available_order:
        order = 1
    tree = BinarySearchTree()
    students = getDataFile()

    for student in students:
        tree.insert(student)

    if order == 3:
        order += 1

    students_tree: list = getTreeData(tree, order)
    file = open(getenv('FILE_OUTPUT_PATH'), 'w')
    for item in students_tree:
        file.write(f"{item}\n")
    file.close()
