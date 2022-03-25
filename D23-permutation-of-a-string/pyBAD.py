class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check=dict()
        lns1=len(s1)
        for ele in s1:
            try:
                check[ele]+=1
            except:
                check[ele]=1
        i=0
        while i < len(s2):
            if s2[i] in check:
                temp=check.copy()
                checked=True
                tempin=i
                for _ in range(lns1):
                    try:
                        if temp[s2[i]] > 1:
                            temp[s2[i]]-=1
                        elif temp[s2[i]] == 1:
                            del(temp[s2[i]])
                    except:
                        i=tempin+1
                        checked=False
                        break
                    i+=1
                if checked==True:
                    if temp=={}:
                        return True
            else:
                i+=1
        return False