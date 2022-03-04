    def backspaceCompare(self, s: str, t: str) -> bool:
        i,j=len(s)-1,len(t)-1
        cnti,cntj=0,0
        while i>=0 and j>=0:
            
            if s[i]=='#':
                cnti+=1
                i-=1
            elif s[i]!='#':
                if cnti !=0:
                    i-=1
                    cnti-=1
            
            if t[j]=='#':
                cntj+=1
                j-=1
            elif t[j]!='#':
                if cntj !=0:
                    j-=1
                    cntj-=1
            if cnti==0 and cntj==0:
                if s[i] != t[j]:
                    return False
                else:
                    i-=1
                    j-=1
            
        return True