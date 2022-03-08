from pip import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ln=len(nums)
        res = [0] * ln
        for i in range(ln):
            res[i]=nums[nums[i]]
        return res