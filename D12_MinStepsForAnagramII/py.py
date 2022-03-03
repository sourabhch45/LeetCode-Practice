class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt=[0]*26
        for ele in s:
            cnt[ord(ele)-ord('a')]+=1
        for ele in t:
            cnt[ord(ele)-ord('a')]-=1
        return(sum(map(abs,cnt)))