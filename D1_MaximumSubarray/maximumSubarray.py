class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n=len(nums)
        maxx= -sys.maxsize -1
        summ=0
        for i in range(0,n):
            summ+=nums[i]
            maxx=max(summ,maxx)
            print(summ,maxx, 'ele=',nums[i])
            if summ<0:
                summ=0
        print(maxx)
        return(maxx)
