def non_constructible_array(nums):
    nums.sort()
    res = []
    i, sum = 0, nums[0]
    while( i + 1 < len(nums)):
        if (nums[i + 1] > sum + 1):
            return sum + 1
        sum += (nums[i+1])
        i += 1

print(non_constructible_array([5,7,1,1,2,3,22]))