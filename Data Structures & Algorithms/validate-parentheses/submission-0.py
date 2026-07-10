class Solution:
    def isValid(self, s: str) -> bool:
        flag = False
        seen = {"[":"]", "{":"}", "(":")"}
        stack = []

        for ch in s:


            if ch in "({[":
                stack.append(ch)
                continue
            
            else:
                if not stack:
                    return flag
                    
                if ch == seen[stack[-1]]:
                    stack.pop()
                
                else:
                    return flag



        if not stack:
            flag = True
        
        return flag


        