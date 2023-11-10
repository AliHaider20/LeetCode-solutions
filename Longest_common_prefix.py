# To find longest common prefix from the each list of words

strs_list = [["flower","flow","flight", "flow"], ["dog","racecar","car"], ["a", "apple", "apply"]]

for strs in strs_list:

	# Getting smallest word
	small_str = strs[0] 

	for i in strs:
		if len(i) < len(small_str):
			small_str = i

	# Function for each length check
	def count_matches(strings, check_length):
		count = 0

		for word in strings:
			if word[:check_length] == small_str[:check_length]:
				count += 1
		
		return count == len(strs)

	for i in range(len(small_str), 0, -1):
		if count_matches(strs, i):
			print(small_str[:i])
			break
	else:
		print("No common sub string")
