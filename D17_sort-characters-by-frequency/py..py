class Solution:
    def frequencySort(self, s: str) -> str:
        seen=dict()
        for ele in s:
            if  ele in seen:
                seen[ele]+=1
            else:
                seen.update({ele:1})
        sorted(seen,key=seen.get,reverse=True)
        print(seen)
        res=''
        for ele in sorted(seen,key=seen.get,reverse=True):
            res+=ele*seen[ele]
        return res