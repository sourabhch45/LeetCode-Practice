[Link](https://leetcode.com/problems/number-of-different-integers-in-a-string/)

# Way better Solution:
Got from discuss
def numDifferentIntegers(self, word):
    s = ''.join(c if c.isdigit() else ' ' for c in word)
    return len(set(map(int, s.split())))