# 1   2  3   4
# 5   6  7   8
# 9  10  11  12
# 13 14  15  16

# def SpiralTraverse(arr):
#     startRow, endRow, startCol, endCol = 0, len(arr), 0, len(arr[0])
    
#     while startRow < endRow and startCol < endCol:

#         for i in range(startCol, endCol):
#             print(arr[startRow][i], end = ' ')
#         print()
#         for i in range(startRow + 1, endRow):
#             print(arr[i][endCol - 1], end = ' ')
#         print()
        
#         for i in reversed(range(startCol, endCol - 1)):
#             print(arr[endRow - 1][i], end = ' ')
#         print()
        
#         for i in reversed(range(startRow + 1, endRow - 1)):
#             print(arr[i][startCol], end = ' ')
#         print()
        
#         startRow += 1
#         startCol += 1
#         endRow   -= 1
#         endCol   -= 1

def Func(arr):
    SpiralTraverse(arr, 0, len(arr), 0, len(arr[0]))

def SpiralTraverse(arr, startRow, endRow, startCol, endCol):
    
    # print(startRow, startCol, endRow, endCol)
    if startRow > endRow or startCol > endCol:
        return
    
    for i in range(startCol, endCol):
        print(arr[startRow][i], end = ' ')
    print()
    for i in range(startRow + 1, endRow):
        print(arr[i][endCol - 1], end = ' ')
    print()
    
    for i in reversed(range(startCol, endCol - 1)):
        print(arr[endRow - 1][i], end = ' ')
    print()
    
    for i in reversed(range(startRow + 1, endRow - 1)):
        print(arr[i][startCol], end = ' ')
    print()
    
    SpiralTraverse(arr, startRow + 1,endRow - 1, startCol + 1, endCol - 1)
# return arr

arr = [[1  ,2   ,3  ,4],
       [5  ,6   ,7  ,8],
       [9  ,10  ,11 ,12],
       [13 ,14  ,15 ,16]]

Func(arr)