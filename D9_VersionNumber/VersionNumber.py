class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split('.')))
        v2=list(map(int,version2.split('.')))
        print(v1,v2)
        ln=max(len(v1),len(v2))
        for i in range(ln):
            try:
                e1 =v1[i]
            except:
                e1=0
            try:
                e2=v2[i]
            except:
                e2=0
            
            if e1>e2:
                return 1
            elif e2 >e1:
                return -1
        return 0