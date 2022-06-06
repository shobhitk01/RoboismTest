nums = [2,8,9,1,8,7,5]
max = 0
res = nums[0]
for i in nums:
	freq = nums.count(i)
	if freq > max:
		max = freq
		res = i
	
print ("Most frequent number is : " + str(res))
