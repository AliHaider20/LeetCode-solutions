def pivotIndex(nums):  
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    else:
        return -1
