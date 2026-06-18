class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        flag = False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(s) != len(t):
            return flag

        if sorted_s == sorted_t:
            flag = True
        
        return flag

