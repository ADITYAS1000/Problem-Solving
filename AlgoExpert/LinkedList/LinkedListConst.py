# DoublyLinkedList

# 1 <- 2 <- 3 <- 4 <-5
#   ->   ->   ->   ->
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.insertBefore(self.head, nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(position, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node # If we do not use this, then along with deleted node..the "next" connection is also deleted. 
                                # Here we update node to next and save the node to remove in some other place as well
            node = node.next
            if nodeToRemove.data == value:
                self.remove(node.data)

    # O(1) time | O(1) space
    def removeKeyBindings(self, node):
        if node.prev is not None:
            node.next.prev = node.prev
        if node.next is not None:
            node.prev.next = node.next
        node.prev = None
        node.next = None

    # O(1) time | O(1) space
    def remove(self, node):
        if(node == self.head):
            self.head = self.head.next
        if(node == self.tail):
            self.tail = self.tail.prev
        self.removeKeyBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        return node is not None

    # O(n) time | O(1) space
    def printLL(self, head):
        while head != None:
            print(head.data, end = " ")
            head = head.next
        print()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4