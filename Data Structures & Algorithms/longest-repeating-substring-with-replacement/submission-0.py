class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        l = 0
        seen = defaultdict(int)
        high = 0

        for right in range(len(s)):
            seen[s[right]] += 1
            high = max(seen.values())
            total = sum(seen.values())
            rep = total - high

            while rep > k:
                seen[s[left]] -= 1
                left += 1
                
                high = max(seen.values())
                total = sum(seen.values())
                rep = total - high
            
            l = max(l, right - left + 1)
        
        return l
            










        