# [-3,-1,2,3,6] => [9,1,4,9,36] => [1,4,9,9,36]

input = [-3,-1,2,3,6]  # Array of Sorted integers
# print(input)
output = []

# T: O(n logn) | S: O(1)
# def SortedArrays(input):
#     for each in range(len(input)):
#         input[each] *= input[each]
#     input = sorted(input)
#     return input

# print(SortedArrays(input))

# T: O(n) | S: O(n)
def SortedArrays(input):
    lst2 = [0 for _ in input]
    smallerIndex = 0
    largerIndex = len(input) - 1
    
    for idx in reversed(range(len(input))):
        smallerValue = input[smallerIndex]
        largerValue  = input[largerIndex]

        if(abs(smallerValue) < abs(largerValue)):
            lst2[idx] = (largerValue * largerValue)
            largerIndex -= 1
        else:
            lst2[idx] = (smallerValue * smallerValue)
            smallerIndex += 1
    return lst2x 

print(SortedArrays(input))