#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [1] * len(nums)
#         postfix = [1] * len(nums)
    
#         result = [1] * len(nums)
    
#         cum_prod = 1
    
#         # prefix[0] = cum_prod
#         for i in range(len(nums)):
#             cum_prod *= nums[i]
#             prefix[i] = cum_prod
#         print(prefix)
    
#         cum_prod = 1
#         for i in reversed(range(0, len(nums))):
#             cum_prod *= nums[i]
#             postfix[i] = cum_prod
#         print(postfix)
    
#         for i in range(len(result)):
#             prefix_data = 1 if i == 0 else prefix[i - 1]
#             postfix_data = 1 if i == len(result) - 1 else postfix[i + 1]
#             result[i] = prefix_data * postfix_data
#         print(result)

def productExceptSelf(nums):
    prefix_arr = [1] * len(nums)
    postfix_arr = [1] * len(nums)
    
    result = [1] * len(nums)
    
    # 1st iteration
    compound_prod = 1
    for i in range(len(nums)):
        prefix = 1 if i == 0 else nums[i - 1]
        compound_prod *= prefix
        result[i] = compound_prod
    
    # 2nd iteration
    compound_prod = 1
    for i in reversed(range(0,len(nums))):
        postfix = 1 if i == len(nums) - 1 else nums[i + 1]
        compound_prod *= postfix
        result[i] *= compound_prod
    
    return result

print(productExceptSelf([1,2,3,4]))