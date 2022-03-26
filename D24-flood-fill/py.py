from pip import List


class Solution:
    newColor=0
    checkColor=0
    image=list()
    def fill(self,r,c):
        
        if self.image[r][c] == self.checkColor and r>=0 and c>=0:
            self.image[r][c] = str(self.newColor)

            try:
                self.fill(r+1,c)
            except:
                pass
            try:
                self.fill(r-1,c)
            except:
                pass
            try:
                self.fill(r,c+1)
            except:
                pass
            try:
                self.fill(r,c-1)
            except:
                pass
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.checkColor=image[sr][sc]
        self.newColor=newColor
        self.image=image
        self.fill(sr,sc)
        res=list()
        for i in range(len(self.image)):
            res.append(list(map(str,self.image[i])))
        return res