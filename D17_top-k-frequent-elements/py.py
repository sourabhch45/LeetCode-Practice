class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=dict()
        for ele in nums:
            if  ele in seen:
                seen[ele]+=1
            else:
                seen.update({ele:1})
        sorted(seen,key=seen.get)
        print(seen)
        res=[]
        cnt=0
        for ele in sorted(seen,key=seen.get,reverse=True):
            if cnt==k:
                break
            res.append(ele)
            cnt+=1
        return res