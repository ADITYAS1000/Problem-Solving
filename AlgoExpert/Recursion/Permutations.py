# # 123
# # 132
# # 213
# # 231
# # 312
# # 321
# # For n, there are n! permutations

# # TIME Complexity: O(n! * n * n) => n! times append to perms, n times call to n! if condition, n times we do the array slicing which is O(n) operation.
# # Space Complexity : O(n * n!) => n is no. of elements in each output permutation, and there are n! permutations.


# # PROBLEM : Can we do better on slicing part? Can we make it a O(1) operation?
# def find_perm(arr, perm, perms):
#     if(len(arr) == 0):
#         perms.append(perm)
#     else:
#         for num in range(0, len(arr)):
#             new_arr = arr[:num] + arr[num+1:] #Slicing
#             newPerm = perm + [arr[num]]
#             find_perm(new_arr, newPerm, perms)

# # TIME Complexity: O(n! * n) => n! times append to perms, n times call to n! if condition, rest array swapping is O(1)
# # Space Complexity : O(n * n!) => n is no. of elements in each output permutation, and there are n! permutations.
# def find_permutation(i,arr, perms):
#     if i == len(arr) - 1:
#         perms.append(arr[:])
#     else:
#         for j in range(i, len(arr)):
#             swap_arr(i,j, arr)
#             find_permutation(i+1, arr, perms)
#             swap_arr(i,j, arr)

# def swap_arr(i,j, arr):
#     arr[i] , arr[j] = arr[j] , arr[i]

# perms = []
# # find_perm([1,2,3], [], perms)
# find_permutation(0, [1,2,3], perms)
# print(perms)

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    if len(s) == 1:
        return s[0]
    return [s[-1]] + [reverseString(s[0:-1])]

def reverseString2(s,l,r):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    if l >= r:
        return s
    s[l],s[r] = s[r],s[l]
    return reverseString2(s,l+1,r-1)

op1 = []
op = reverseString2(['h','e','l','l','o'],0,4)
print(op)