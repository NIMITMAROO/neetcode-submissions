class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        flag = False
        i = 0

        if len(s) != len(t):
            return flag
        
        else:

            while i != len(s):
                
                if s[i] in t:
                    t = t.replace(s[i], "", 1)
                i += 1
            
            if t == "":
                flag = True
            return flag