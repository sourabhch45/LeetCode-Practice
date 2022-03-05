from pip import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        indi,indj=0,0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    indi=i
                    indj=j
        res=0
        for i in range(indi,-1,-1): #up
            if board[i][indj] == 'p':
                res+=1
                print(i,indj)
                break
            elif board[i][indj] == 'B':
                break
        for i in range(indi,8): #down
            if board[i][indj] == 'p':
                res+=1
                print(i,indj)
                break
            elif board[i][indj] == 'B':
                break
        for j in range(indj,8): #right
            if board[indi][j] == 'p':
                res+=1
                print(i,indj)
                break
            elif board[indi][j] == 'B':
                break
        for j in range(indj,-1,-1): #left
            if board[indi][j] == 'p':
                res+=1
                print(i,indj)
                break
            elif board[indi][j] == 'B':
                break
        return res