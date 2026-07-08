class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        flag = False 
        seen = defaultdict(int)
        window = defaultdict(int)

        if len(s1) > len(s2):
            return flag

        for ch in s1:
            seen[ch] += 1
        
        for i in range(len(s1)):
             window[s2[i]] += 1 

        if window == seen:
            flag = True
            return flag

        while right < len(s2) - 1:

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
            right += 1

            window[s2[right]] += 1
            if seen == window:
                flag = True
                return flag


        return flag



        