class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        stind=0
        res=set()
        ln=len(word)
        if ln ==1 and word[0] in '1234567890':

            return 1
        for i in range(1,ln):
            if i == 1 and word[0] in '1234567890':
                stind =0
            if word[i-1] in 'abcdefghijklmmnopqrstuvwxyz' and word[i] in '1234567890'  :
                stind=i
            if word[i-1] in '1234567890' and word[i] in 'abcdefghijklmmnopqrstuvwxyz':
                res.add(int(word[stind:i]))
            if i==len(word)-1 and word[i] in '1234567890':
                res.add(int(word[stind:]))
        print(res)
        return(len(res))                