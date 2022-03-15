from pip import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lis=[0]*26
        for ele in chars:
            lis[ord(ele)-ord('a')]+=1
        res=0
        print(lis)
        for word in words:
            tplis=[]
            for ele in lis:
                tplis.append(ele)
            good=True
            for ele in word:
                if tplis[(ord(ele)-ord('a'))] == 0:
                    good=False
                if tplis[(ord(ele)-ord('a'))] != 0:
                    tplis[(ord(ele)-ord('a'))]-=1
            if  good == True:
                res+=len(word)
        return res