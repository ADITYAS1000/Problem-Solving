# Recursive Solution:
# O(n * 2^n) | O(n * 2^n)
# def powersets(input):
#     subsets = [[]]
#     for element in input:
#         for i in range(len(subsets)):
#             currentSubset = subsets[i]
#             subsets.append(currentSubset + [element])
#     return subsets



# Iterative Solution:
# O(n * 2^n) | O(n * 2^n)
def powersets(input,idx = None):
    if idx is None:
        idx = len(input) - 1
    if idx < 0:
        return [[]]
    element = input[idx]

    subsets = powersets(input, idx - 1)

    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [element])
    return subsets

op = powersets([1,2,3])
print(op)