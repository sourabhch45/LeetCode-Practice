class Solution:
    def reformatNumber(self, number: str) -> str:
        filt=''
        for ele in number:
            if ele in '0123456789':
              filt+=ele
        ln = len(filt)
        res=''
        ind=ln
        if ln %3 == 1:
            res=f'{filt[-3:-5:-1][::-1]}-{filt[-1:-3:-1][::-1]}'
            ind = ln-5
        if ln %3 == 2:
            res = f'{filt[-1:-3:-1][::-1]}'
            ind = ln-2
        for i in reversed(range(0,ind,3)):
            
            res= filt[i:i+3]+ '-' + res
        if ln%3 == 0:
            res=res[0:-1]
        return res