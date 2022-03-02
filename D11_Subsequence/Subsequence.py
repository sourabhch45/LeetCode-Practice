class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        key=0
        for ind in range(len(t)):
            if  key ==len(s):
                return True
            if t[ind]==s[key]:
                key+=1
                print(key)
        if  key ==len(s):
                return True
        if key<len(s):
            return False