class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = defaultdict(list)
        flag = True

        if len(s) != len(t):
            flag = False
            return flag
        
        for char1 in s:
            anagram[char1] = anagram.get(char1, 0) + 1
        
        for char2 in t:
            anagram[char2] = anagram.get(char2, 0) - 1
        
        for value in anagram.values():
            if value != 0:
                return False
        
        return flag
