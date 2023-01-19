# [3,5,-4,8,11,1,-1,6] target = 10

# Avoid O(n^2)
# Print pair of two numbers which sum upto target

# array sorted? : No, but you can
# are negatives allowed? : Yes
# can array be empty? : No

# Approach 1: (Iterative) O(n^2) | O(1)
# def SumOfTwo(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [arr[i] , arr[j]]

# Two pointer approach [1,2,3,4,5] T = 6 : i,j .. i<j if i+j == target save.. i++ j-- .. (i + j) < target i++ (i + j) > target j--

# O(n) | O(1)
# def SumOfTwo(arr, target):
#     arr.sort()
#     result = []

#     l,r = 0, len(arr) - 1

#     while l < r:
#         if (arr[l] + arr[r]) > target:
#             r = r - 1
#         elif (arr[l] + arr[r]) < target:
#             l = l + 1
#         else:
#             result.append([arr[l],arr[r]])
#             l, r = l+1, r-1
#     return result

# lst = [5,3,4,1,2] #   In 2 pointer approach, sorting of list DOES matter.. gives only [5,1]
# lst = [1,2,3,4,5] #   gives both [1,5] and [2,4]
# target = 6
# lst = [-4, 5, 11, 8,3,1,-1,6]
# target = 10

# Appraoch 3: Hashmap
# O(n) T | O(n) S
def SumOfTwo(arr, target):
    hashmap = {}
    result = []
    for element in arr:
        complement = target - element
        if complement in hashmap:
            print(hashmap)
            result.append([complement,element])
            del hashmap[complement]
        else:
            hashmap[element] = True
    return result

# O(n) T | O(n) S
# Complement approach
# def SumOfTwo(lst, target):
#     hashmap = {}
#     complement = 0
#     result = []
#     for index in range(0,len(lst)):
#         element = lst[index]
#         complement = target - element
#         if(element in hashmap):
#             result.append((element, complement))
#             del hashmap[element]
#         else:
#             hashmap[complement] = index
#     return result

lst = [3, 5, -4,11, 8,-1,1,11,-1,6] # there are 2 pairs : 11,-1...11,-1 . 2 outputs .. 11,-1 , 11,-1
lst = [3, 5, -4,11, 8,-1,1,11,6]    # 1 output .. 11,-1 since on getting pair, we delete hashmap entry meaning there can be another output only if there is another 11 and -1 in input
target = 10

print(SumOfTwo(lst, target))