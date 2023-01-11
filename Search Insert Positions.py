def searchInsert(nums, target):
      if target in nums:
          return nums.index(target)

      for i in range(len(nums)):
          if nums[i-1] < target < nums[i]:
              return i
          elif nums[i]>target:
              return i
          elif nums[-1] < target:
              return len(nums)
