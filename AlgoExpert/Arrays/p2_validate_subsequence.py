lst_input = [5,1,22,25,6,-1,8,10]
lst_check = [1,6,-1,10]


# T : O(m * log(n+m)) | S: O(1)
# def ValidateSubsequence(lst_input, lst_check):
#     for index in range(0,len(lst_check)):
#         print(lst_input[index], lst_check[index])
#         if(lst_input[index] != lst_check[index]):
#             return False
#     return True 

# T : O(n) | S : O(1)
def ValidateSubsequence(lst_input, lst_check):
    seqIdx = 0
    for value in lst_input:
        if(seqIdx == len(lst_check)):
            break
        if(value == lst_check[seqIdx]):
            seqIdx += 1
            print(value, seqIdx)
    return seqIdx == len(lst_check)

print(ValidateSubsequence(lst_input, lst_check))