class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for ele in s:
            if res!=[] and res[-1]==ele:
                res.pop()
            else:
                res.append(ele)
        return ''.join(res)
