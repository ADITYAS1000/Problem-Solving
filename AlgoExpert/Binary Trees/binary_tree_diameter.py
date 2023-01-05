from binarytree import Node

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def getDiameter(node):
    return getTreeInfo(node).diameter

def getTreeInfo(node):
    if node is None:
        return TreeInfo(0,0)
    
    leftTree  = getTreeInfo(node.left)
    rightTree = getTreeInfo(node.right)
    
    maxDiameter = max(leftTree.diameter, rightTree.diameter)
    LongestPathThroughRoot = leftTree.height + rightTree.height
    
    currentDiameter = max(maxDiameter, LongestPathThroughRoot)
    currentHeight   = 1 + max(leftTree.height, rightTree.height)

    return TreeInfo(currentDiameter, currentHeight)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.left  = n3
n1.right = n2
n3.left  = n7
n7.left  = n8
n8.left  = n9
n3.right = n4
n4.right = n5
n5.right = n6

print(n1)

diameter = getDiameter(n1)

print(diameter)