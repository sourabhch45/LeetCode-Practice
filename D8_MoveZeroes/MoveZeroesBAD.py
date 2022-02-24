from pip import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=0
        count=0
        while count < (len(nums)):
            if nums[ind]==0:
                del(nums[ind])
                nums.append(0)
                print(nums)
                count+=1
            else:
                ind+=1            
                count+=1