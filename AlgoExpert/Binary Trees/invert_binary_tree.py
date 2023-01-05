from binarytree import Node

# O(n) time: Iterate over all nodes in array | O(n) space in queue..there will be n/2 leaf nodes in queue, giving O(n) space
def iter_invert_tree(node):
    if node is None:
        return
    queue = []
    queue.append(node)

    while len(queue):
        node = queue.pop(0)
        if node is None:
            return
        node.right, node.left = node.left, node.right
        queue.append(node.left)
        queue.append(node.right)



# O(n) time - Traversal through every node | O(d) space - D recursive calls based on D depth of tree.
def invert_tree(node):
    if node is None:
        return
    
    node.right, node.left = node.left, node.right

    invert_tree(node.left)
    invert_tree(node.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left  = n2
n1.right = n3
n2.left  = n4
n2.right = n5
n3.right = n6
# n3.left  = None

print(n1)

# invert_tree(n1)
iter_invert_tree(n1)

print(n1)