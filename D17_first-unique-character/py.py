class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen=dict()
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]]+=1
            elif s[i] not in seen:
                seen.update({s[i]:1})
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        else:
            return -1