import random
from numpy import median


class CompratorNode:
    def __init__(self, value, dimension, parent=None, leftChild=None, rightChild=None):
        self.value = value
        self.dimension = dimension
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

    def setParent(self, parent):
        self.parent = parent

    def addRightChild(self, right):
        self.rightChild = right

    def addLeftChild(self, left):
        self.leftChild = left


class LeafNode:
    def __init__(self, parent, values=[]):
        self.parent = parent
        self.values = values

    def addParent(self, parent):
        self.parent = parent

    def addValue(self, *args):
        for point in args:
            self.values.append(point)


class Tree:
    def __init__(self, points, dimension, leafPointsCount):
        self.points = points
        self.dimension = dimension
        self.leafNodeCount = leafPointsCount
        self.nodes = []

    def createTree(self):
        return self.__makeTree(self.points)

    def __makeTree(self, points, parent=None):

        selectedDim = random.randint(0, self.dimension-1)

        if len(points) <= self.leafNodeCount:
            leafNode = LeafNode(parent, points)
            return leafNode

        speceficDimonList = [n[selectedDim] for n in points]
        # print(speceficDimonList)
        mid = int(median(speceficDimonList))

        # print(mid,selectedDim)

        leftPoints = []
        rightPoints = []

        for point in points:
            if point[selectedDim] <= mid:
                leftPoints.append(point)
            else:
                rightPoints.append(point)

        node = CompratorNode(mid, selectedDim, parent)

        self.nodes.append(node)

        node.addLeftChild(self.__makeTree(leftPoints, node))
        node.addRightChild(self.__makeTree(rightPoints, node))

        return node


def main():
    l = []
    for i in range(400):
        i = []
        for j in range(96):
            i.append(random.randint(0, 255))

        l.append(i)

    t = Tree2(l, 5, 10)


main()
