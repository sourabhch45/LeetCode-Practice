class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        data=[]
        for ind,ele in enumerate(reversed(columnTitle)):
            data.append((ord(ele)-64)*(26**ind))
        return sum(data)