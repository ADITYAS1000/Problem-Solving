from distutils.errors import DistutilsFileError
import sys

# Need to do push, pop, peek, getmin, getMax in O(1) time and O(1) space

class MinMaxStack:
    
    def __init__(self):
        self.MinMaxStack = []
        self.stack = []

    def push(self, number):
        minMax = {"min": number, "max" : number}
        if(len(self.MinMaxStack)):
            lastMinMax = self.MinMaxStack[len(self.MinMaxStack) - 1]
            minMax["min"] = min(lastMinMax["min"],number)
            minMax["max"] = max(lastMinMax["max"],number)
        self.MinMaxStack.append(minMax)
        self.stack.append(number)

    def pop(self):
        self.MinMaxStack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def min(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["min"]

    def max(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["max"]
    
    def printStack(self):
        for x in self.stack: print(x)

s1 = MinMaxStack()
print("After init")
s1.printStack()
s1.push(4)
print("After push")
s1.push(3)
print("After push")
s1.push(2)
print("After push")
s1.push(1)
print("After push")
s1.printStack()
s1.pop()
print("After pop")
s1.printStack()
print("After peek")
print(s1.peek())
print("After min")
print(s1.min())
print("After max")
print(s1.max())