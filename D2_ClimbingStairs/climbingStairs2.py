import math
class Solution:
    def climbStairs(self, n: int) -> int:
        fib=[]
        for i in range(n+1):
            if i == 0 or i== 1:
                fib.append(1)
            else:
                fib.append(fib[i-1]+fib[i-2])
            # if i==n:
            #     break
        return fib[n]
