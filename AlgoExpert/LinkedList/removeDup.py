# 1,1,2,2,3,3

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(2)
n5 = Node(3)
n6 = Node(3)

n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n5.next = n6;

def printLL(head):
    while head != None:
        print(head.data)
        head = head.next

def removeDup(head):
    currentNode = head
    while currentNode is not None:
        nextDistinct = currentNode.next
        while nextDistinct is not None and nextDistinct.data == currentNode.data:
            nextDistinct = nextDistinct.next
        currentNode.next = nextDistinct
        currentNode = nextDistinct
    return head

# def removeDup(head):
#     currentNode = head
#     while currentNode.next != None:
#         if currentNode.next.data == currentNode.data:
#             temp = currentNode.next.next
#             currentNode.next = temp
#         else:
#             currentNode = currentNode.next
#     return head

head = removeDup(n1)
printLL(head)