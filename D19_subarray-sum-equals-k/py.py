from pip import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ln=len(nums)
        seen={0:1}
        sum=0
        res=0
        for i in range(ln):
            sum+=nums[i]
            if sum-k in seen.keys():
                res+=seen[sum-k]
            if sum in seen.keys():
                seen[sum]+=1
            elif sum not in seen.keys():
                seen.update({sum:1})
        return res
            