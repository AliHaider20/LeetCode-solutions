nums = [-1,1,0,-3,3]
output = [0,0,9,0,0] # Expected output

temp = []

if 0 in nums: # Checking if the nums array contains 0
	for i in range(len(nums)): 
		prod = 1
		if nums[i] == 0:
			for j in range(0, i): # Multiplying elements present at the LHS of 0
				prod *= nums[j]
			for j in range(i+1, len(nums)): # Multiplying elements present at the RHS of 0
				prod *= nums[j]
			temp.append(prod)
		else:
			temp.append(0) # Appending 0 as the array contains 0
else:
	prod = 1
	for j in nums: # Multiply all the elements
		prod *= j
	for i in nums:
		temp.append(int(prod/i)) # Divide the current