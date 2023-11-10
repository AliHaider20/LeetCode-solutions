nums = [1,7,3,6,5,6]

def pivot(arr):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    else:
        return -1
pivot(nums)
