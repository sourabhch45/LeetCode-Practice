# link: https://leetcode.com/problems/permutation-in-string/submissions/
# Help from: https://leetcode.com/problems/permutation-in-string/discuss/1762469/C%2B%2B-oror-SLIDING-WINDOW-OPTIMIZED-oror-Well-Explained
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fs1=[0]*26
        lns1,lns2=len(s1),len(s2)
        for ele in s1:
            fs1[ord(ele)-ord('a')]+=1
        fs2=[0]*26
        i=j=0
        while j<lns2:
            fs2[ord(s2[j])-ord('a')]+=1
            
            if j-i+1==lns1:
                if fs1==fs2:
                    return True
                
            if j-i+1<lns1:
                j+=1
                
            else:
                fs2[ord(s2[i])-ord('a')]-=1
                i+=1
                j+=1
        return False 