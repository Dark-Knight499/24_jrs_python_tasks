class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        x = 26*[0]
        for i in magazine:
            x[ ord(i) - ord("a")]+=1
        for i in ransomNote:
            if x[ ord(i) - ord("a")] == 0:
                return False
            else:
                x[ ord(i) - ord("a")]-=1
        return True  