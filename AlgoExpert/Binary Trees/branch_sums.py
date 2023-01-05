from contextlib import nullcontext
from multiprocessing.sharedctypes import Value
from binarytree import Node

class BranchSum:

    # O(n) time | O(n) Space : apart from traversal.. the output is an array of depth N 
    def calcSum(self, node, RunningSum, sums):

        if node is None:
            return

        newRunningSum = RunningSum + node.value

        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return
        
        self.calcSum(node.left, newRunningSum, sums)
        self.calcSum(node.right, newRunningSum, sums)

    def getSum(self,root):
        sums = []
        sum = self.calcSum(root, 0, sums)
        return sums

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left  = n2
n1.right = n3
n2.left  = n4
n2.right = n5

print(n1)
b = BranchSum()
sum = b.getSum(n1)
print(sum)