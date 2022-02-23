from pip import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        strtin=0
        count=0
        if len(nums)==1:
            return(nums[0])
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                #count=max(count,(i)-strtin)
                if (i)-strtin > count:
                    count=(i)-strtin
                    res=nums[i-1]
                strtin=i
            if i==len(nums)-1:
                if ((len(nums))-strtin) >count:
                    res=nums[-1]
        return(res)