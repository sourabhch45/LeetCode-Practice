from pip import List


def kLengthApart(self, nums: List[int], k: int) -> bool:
    diff=0
    try:
        ind=nums.index(1)
    except:
        return True
    for i in range(ind+1,len(nums)):
        
        if nums[i]==1:
            print(i,diff)
            if diff < k:
                print('falsed',diff,k)
                return False
            diff=0
        if nums[i]==0:
            diff+=1
    return True