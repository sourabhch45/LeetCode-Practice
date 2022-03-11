from ast import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ln=len(nums)
        lsum=0
        rsum=sum(nums[1:])
        for i in range(ln):
            print(lsum,rsum)
            if rsum == lsum:
                return i
            lsum+=nums[i]
            try:
                rsum-=nums[i+1]
            except:
                rsum=0
        else:
            return -1