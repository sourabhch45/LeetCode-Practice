from pip import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ansind=0
        count=1
        for i in range(1,len(nums)):
            
            if nums[i]==nums[ansind]:
                count+=1
            elif nums[i]!=nums[ansind]:
                count-=1
            if count == 0:
                ansind=i
                count=1
        return nums[ansind]