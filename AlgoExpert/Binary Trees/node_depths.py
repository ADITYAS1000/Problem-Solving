from binarytree import Node

# Time : O(n), Space : O(h) - height of binary tree
def IterCalcDepth(node):
    sumOfDepths = 0
    nodeMap = [{"node":node, "depth" : 0}]
    while nodeMap:
        nodeInfo = nodeMap.pop()
        val, depth = nodeInfo["node"].value, nodeInfo["depth"]
        if val is None:
            continue
        sumOfDepths += depth
        nodeMap.append({"node":node.right, "depth" : depth + 1})
        nodeMap.append({"node":node.left, "depth" : depth + 1})
    return sumOfDepths

# # Time: O(n) | Space: O(h) - height of binary tree
# def calcDepth(node, input_count = 0):
#     global sum
#     if node is None:
#         return
#     sum = sum + input_count
#     calcDepth(node.left, input_count + 1)
#     calcDepth(node.right, input_count + 1)

# Time: O(n) | Space: O(h) - height of binary tree
def calcDepth(node, depth = 0):
    if node is None:
        return 0
    return depth + calcDepth(node.left, depth + 1) + calcDepth(node.right, depth + 1)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.left  = n2
n1.right = n3
n2.left  = n4
n2.right = n5
n3.left  = n6
n3.right = n7
n4.left  = n8
n4.right = n9

print(n1)
sum = calcDepth(n1)
print(sum)
