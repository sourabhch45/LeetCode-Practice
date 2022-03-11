from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        for ele in nums:
            nums[abs(ele)-1] = -1*abs(nums[ele-1] )
        res=[]
        for i in range(ln):
            if nums[i]>0:
                res.append(i+1)
        return res