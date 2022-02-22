nums=[1,2,12,2,1,4,4]
nums=sorted(nums)
for i in range(1,len(nums),2):
    if nums[i-1]!=nums[i]:
        print(nums[i-1])
else:
    print(nums[-1])