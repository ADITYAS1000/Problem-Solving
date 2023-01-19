lst_input = [5,1,22,25,6,-1,8,10]
lst_check = [1,6,-1,10]


# O(n) | O(1) : For loop solution
# def ValidateSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if value == sequence[seqIdx]:
#             seqIdx += 1
#     return seqIdx == len(sequence)


# T : O(n) | S : O(1) : While loop solution
def ValidateSubsequence(array, sequence):
    seqIdx, arrayIdx = 0, 0
    while seqIdx < len(sequence) and arrayIdx < len(array):
        if sequence[seqIdx] == array[arrayIdx]:
            seqIdx += 1
            arrayIdx += 1
        else:
            arrayIdx += 1
    return seqIdx == len(sequence)

print(ValidateSubsequence(lst_input, lst_check))