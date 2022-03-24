from __future__ import print_function
from os import getenv
from dotenv import load_dotenv


class Node:
    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

    # get & set functions
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        new_node = Node(label.replace(';', '').replace('|', ','), None)
        if self.empty():
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    def traversalTree(self, traversalFunction=None, root=None):
        if(traversalFunction is None):
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str


def orderBy(node, key: int):
    return node.split(',')[key]


def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList

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
    t = BinarySearchTree()
    students = getDataFile()

    for student in students:
        t.insert(student)

    if order == 3:
        order += 1

    list = sorted(t.traversalTree(InPreOrder, t.root),
                  key=lambda node: orderBy(node, order - 1))
    file = open(getenv('FILE_OUTPUT_PATH'), 'w')
    for item in list:
        file.write(f"{item}\n")
    file.close()
