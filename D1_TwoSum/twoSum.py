class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for curpos,ele in enumerate(nums):
            req=target-ele
            if req < 0:
                pass
            if req in nums:
                return [curpos,nums.index(req)]
