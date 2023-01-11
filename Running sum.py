def runningSum(nums):
    t = 0
    s =[]
    for n in nums:
        t+=n
        s.append(t)
    return s
