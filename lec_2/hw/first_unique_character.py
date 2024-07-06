class Solution(object):
    def firstUniqChar(self, s):
        x = 26*[0]
        for i in s:
            x[ ord(i) - ord("a")]+=1
        for i in range(len(s)):
            if x[ ord(s[i]) - ord("a")] == 1:
                return i
        return -1