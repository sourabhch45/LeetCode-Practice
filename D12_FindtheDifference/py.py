class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt=[0]*26
        for ele in t:
            cnt[ord(ele)-ord('a')]+=1
        for ele in s:
            cnt[ord(ele)-ord('a')]-=1
        ind=cnt.index(1)
        
        return(chr(ind+97))