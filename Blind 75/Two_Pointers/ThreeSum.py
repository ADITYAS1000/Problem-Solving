def threeSum(nums):
    res = []
    nums.sort()
    
    for i,data in enumerate(nums):
        # Move data through duplicates
        if i > 0 and data == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            threeSum = data + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([data, nums[l], nums[r]])
                l += 1
                # Move left index through duplicates
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

print(threeSum([-3,0,1,3,5,2,-2]))