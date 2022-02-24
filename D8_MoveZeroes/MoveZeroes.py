nums=[0,1,0,3,9]
inspt=0
ptr=0
temp=0
while ptr<(len(nums)):
    if nums[ptr] != 0:
        temp=nums[ptr]
        nums[ptr]=0
        ptr+=1
    elif nums[ptr] == 0:
        ptr+=1
    if nums[inspt] ==0 and temp !=0:
        nums[inspt]=temp
        inspt+=1
        temp=0
    elif nums[inspt] != 0:
        inspt+=1
                