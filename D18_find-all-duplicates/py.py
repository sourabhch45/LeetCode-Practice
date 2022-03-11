from pip import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ln=len(nums)
        seen=[0]*ln
        res=[]
        for ele in nums:
            seen[ele-1]+=1
        for i in range(ln):
            if seen[i] ==2:
                res.append(i+1)
        return res