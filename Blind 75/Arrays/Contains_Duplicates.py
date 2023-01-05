# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         current, last = 0, len(nums) - 1
#         my_dict = {}
#         for value in nums:
#             if value not in my_dict:
#                 my_dict[value] = 1
#             else:
#                 my_dict[value] += 1
#             if (my_dict[value] > 1):
#                 return True
#         return False

def containsDuplicate(nums):
    unique = set()
    for each in nums:
        if each in unique:
            return True
        unique.add(each)
    return False

print(containsDuplicate([1,2,3,1]))