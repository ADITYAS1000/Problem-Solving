class Node():
    def __init__(self, value):
        self.value = value;
        self.left = None;
        self.right = None;

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d') 
e = Node('e')
f = Node('f')
g = Node('g')

a.left  = b;
a.right = c;
b.left  = d;
b.right = e;
c.right = f;
c.left  = g;

#         a
#       /   \
#      b     c
#     / \   / \ 
#    d   e g   f   

# O(n) | O(n)
def DFS_Preorder(root): # abdecf
    stack = [root]

    while(len(stack) > 0):
        data = stack.pop()

        print(data.value, end=" ")

        if(data.right is not None):
            stack.append(data.right)
        
        if(data.left is not None):
            stack.append(data.left)
    print()

# O(n) | O(n)
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
def DFS_Inorder(root): # dbeagcf
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.value, end = " ")
            current = current.right    
        else:
            break
    print()

# O(n) | O(n) - 2 stacks
def postOrderIterative(root):
 
    if root is None:
        return       
     
    # Create two stacks
    s1 = []
    s2 = []
     
    # Push root to first stack
    s1.append(root)
     
    # Run while first stack is not empty
    while s1:
         
        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
 
        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.value,end=" ")
    print()


def PostOrderOneStack(root):
    if(root == None):
        return None
    pre = None
    stack = []
    while(root != None or len(stack) > 0):
        if(root is not None):
            stack.append(root)
            root = root.left
        else:
            root = stack[-1]
            if(root.right is None or root.right == pre):
                print(root.value, end = " ")
                stack.pop()
                pre = root
                root = None
            else:
                root = root.right
    print()

def DFS_Inorder_Recursive(root):
    if root is None:
        return None
    DFS_Inorder_Recursive(root.left)
    print(root.value, end = " ")
    DFS_Inorder_Recursive(root.right)

def DFS_Preorder_Recursive(root):
    if root is None:
        return None
    print(root.value, end = " ")
    DFS_Preorder_Recursive(root.left)
    DFS_Preorder_Recursive(root.right)

def DFS_Postorder_Recursive(root):
    if root is None:
        return None
    DFS_Postorder_Recursive(root.left)
    DFS_Postorder_Recursive(root.right)
    print(root.value, end = " ")

# DFS_Preorder(a)
# DFS_Inorder(a)
# postOrderIterative(a)
# PostOrderOneStack(a)

DFS_Postorder_Recursive(a)