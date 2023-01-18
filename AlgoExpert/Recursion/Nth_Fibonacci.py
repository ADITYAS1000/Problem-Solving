# /*
# 0,1,1,2,3,5,8,13,21,34
# */

# Time : O(2^n) : For Nth fibo, there will be 2^n splittings/recursive calls,
# Space: O(n)   : N recursive calls, N to 1.. leading to N space complexity 

# def fibonacci(n):
#     if (n == 1):
#         return 0
#     elif (n == 2):
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# Time : O(n) : Here there will be 2^n splits too, but now using memoize, we avoid redundant recusive calls
# Space: O(n) + O(n) : N call stacks and N values in memoize.. 2N ~ N

# def fibonacci(n, memoize = {1 : 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = fibonacci(n - 1, memoize) + fibonacci(n - 2, memoize)

# Time : O(n) : Go though 3 to N.. hence N
# Space: O(1) : at a point of time, we are updating only 2 elements in list, const. time operation.. hence O(1)

def fibonacci(n):
    arr = [0, 1]
    next = 0
    counter = 3
    while counter <= n:
        next = arr[0] + arr[1]
        arr[0], arr[1] = arr[1] , next
        counter += 1
    return arr[1] if n > 1 else arr[0]

print(fibonacci(2))