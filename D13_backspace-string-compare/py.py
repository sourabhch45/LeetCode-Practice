class Solution:
    
    def getRes(self,s:str):
        ln=len(s)
        cnt=0
        res=''
        for i in reversed(range(0,ln)):
            print(i)
            c=s[i]
            if c=='#':
                cnt+=1
            else:
                if cnt>0:
                    cnt-=1
                else:
                    res+=c
        return res
    
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getRes(s)==self.getRes(t)
        # res=self.getRes(s)