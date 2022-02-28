class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stind=0
        res=[]
        ln=len(nums)
        if ln ==1:
            return [str(nums[0])]
        for i in range(1,ln):
            print(f'res={res},stind={stind},i={i},valuern={nums[i]}')
            if nums[i]!=nums[i-1]+1:
                if stind != i-1:
                    res.append(f'{nums[stind]}->{nums[i-1]}')
                    stind=i
                elif stind == i-1:
                    res.append(str(nums[i-1]))
                    stind=i
            if i==ln-1:
                if stind != i:
                    res.append(f'{nums[stind]}->{nums[i]}')
                if stind == i:
                    res.append(str(nums[stind]))
        return res