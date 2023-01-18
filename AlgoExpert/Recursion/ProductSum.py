# O(n) | O(D) - depth of recursive calls based on levels of sub-array
def rec_ProdSum(arr, multiplier = 1):
    sum = 0
    for element in arr:
        if type(element) is list:
            sum += rec_ProdSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

print(rec_ProdSum([5,2,[7,-1],3,[6,[-13,8],4]]))