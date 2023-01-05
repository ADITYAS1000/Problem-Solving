# [3,5,-4,8,11,1,-1,6] target = 10

# Avoid O(n^2)
# Print pair of two numbers which sum upto target

# array sorted?
# are negatives allowed?
# can array be empty?

# Two pointer approach [1,2,3,4,5] T = 6 : i,j .. i<j if i+j == target save.. i++ j-- .. (i + j) < target i++ (i + j) > target j--

# O(nlog(n)) T | O(1) S
# def SumOfTwo(lst, target):
#     result = []
#     i, j = 0, len(lst) - 1

#     while(i < j):
#         if((lst[i] + lst[j]) == target):
#             result.append((lst[i], lst[j]))
#             i+=1
#             j-=1
#         elif((lst[i] + lst[j]) < target):
#             i += 1
#         else:
#             j -= 1
#     return result

# # lst = [5,4,3,2,1] #   In 2 pointer approach, sorting of list does not matter.. the order of pair is changed depending if input if descending or ascending
# #                       For random ordered input, pairs are based on insertion order
# # target = 6
# lst = [3, 5, -4, 8,11,1,-1,6]
# target = 10


# O(n) T | O(n) S
# Complement approach
def SumOfTwo(lst, target):
    hashmap = {}
    complement = 0
    result = []
    for index in range(0,len(lst)):
        element = lst[index]
        complement = target - element
        if(element in hashmap):
            result.append((element, complement))
            del hashmap[element]
        else:
            hashmap[complement] = index
    return result

lst = [3, 5, -4,-1, 8,11,1,11,-1,6] # there are 2 pairs : 11,-1...11,-1 . 2 outputs .. 11,-1 , 11 : 1 pair since for 2nd time, -1 got matched and didn't create entry in dict
target = 10

print(SumOfTwo(lst, target))