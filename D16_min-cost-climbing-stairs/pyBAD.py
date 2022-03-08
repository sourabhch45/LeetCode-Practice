from ast import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ptr=cost.index(min(cost[0],cost[1]))
        res=0
        ln=len(cost)
        while ptr<ln:
            print(f'value={cost[ptr]} ptr={ptr}')
            if ptr==ln-1 or ptr == ln-2:
                res+=cost[ptr]
                break
            res+=cost[ptr]
            if cost[ptr+1]  == cost[ptr+2]:
                ptr+=2
            elif cost[ptr+1]  < cost[ptr+2]:
                ptr += 1
            elif cost[ptr+1]  > cost[ptr+2]:
                ptr +=2
        return res