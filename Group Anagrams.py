strs = ["eat","tea","tan","ate","nat","bat"] # Test case

final = [[strs[0]]]
for j in range(1, len(strs)):
    str = strs[j]
    for i in range(len(final)):
        if len(final[i][0]) != len(str):
            continue
        if sorted(final[i][0]) == sorted(str):
            final[i].append(strs[j])
            break
    else:
        final.append([strs[j]])

print(final)

# Solution 2

# strs_dict = {}
# for i in strs:
#     sorted_str = "".join(sorted(i))
#     # print(sorted_str)

#     if sorted_str not in strs_dict:
#         strs_dict[sorted_str] = [i]
#     else:
#         strs_dict[sorted_str].append(i)
# print(list(strs_dict.values()))
