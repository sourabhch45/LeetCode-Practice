class Solution:
    def countEven(self, num: int) -> int:
        if num %2 == 1:
            return int(num/2)
        elif num%2 == 0:
            summ=sum([int(temp) for temp in str(num)])
            if summ%2 != 0:
                return (int(num/2)-1)
            elif summ%2 ==0:
                return (int(num/2))