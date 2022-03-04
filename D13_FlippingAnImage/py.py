from pip import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for ele in image:
            ele=reversed(ele)
            temp=[]
            for subele in ele:
                temp.append(1-subele)
            res.append(temp)
        return(res)